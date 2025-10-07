from django.shortcuts import get_object_or_404, redirect, render
from .models import Product,employee
from .forms import ProductForm, CarForm
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse 
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST,require_http_methods



# Create your views here.
@login_required(login_url='/login')
def show_name(request):
    filter_type = request.GET.get("filter", "all")  

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    person = {
        'App_name' : "BluR Sport",
        'name' :'Antonius Daniel',
        'npm' : '2406496012',
        'class' : 'PBP E',
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'username': request.user.username,
        'products' : product_list,

    }
    return render(request, "main.html", person)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        form.save()
        return redirect('main:show_name')

    context = {"form" : form}
    return render(request,"form.html",context)

def create_car(request):
    form = CarForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main : show_name")
    
    context = {"form" : form}
    return render(request,"carform.html",context)

@login_required(login_url='/login')
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "detail.html", {"product": product})

def show_xml(request):
    products = Product.objects.all()
    xml_data = serializers.serialize("xml" , products)
    return HttpResponse(xml_data, content_type="application/xml")

def show_xml_by_id(request, prod_id):
   try:
       product = Product.objects.filter(pk=prod_id)
       xml_data = serializers.serialize("xml", product)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json(request):
    products = Product.objects.all()
    data = [
        {
            'id': str(p.id),  
            'user_id': p.user.id if p.user else None,  
            'user': p.user.username if p.user else None,  
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'thumbnail': p.thumbnail,
            'category': p.category,
            'is_featured': p.is_featured,
        }
        for p in products
    ]
    return JsonResponse(data, safe=False)

def show_json_by_id(request, prod_id):
    try:
        product = Product.objects.select_related('user').get(pk=prod_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured if hasattr(product, 'is_featured') else False,
            'user_id': product.user.id if product.user else None,
            'user_username': product.user.username if product.user else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
   
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Akun anda berhasil dibuat!.')
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'status': 'success', 
                    'message': 'Akun anda berhasil dibuat.',
                    'redirect_url': reverse('main:login')
                }, status=201)
           
            
            return redirect('main:login')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                errors = dict(form.errors.items()) 
                return JsonResponse({
                    'status': 'error', 
                    'message': 'Registration failed. Please check the errors.', 
                    'errors': errors
                }, status=400)
            
            
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response_target = HttpResponseRedirect(reverse("main:show_name"))
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                response_data = {
                    'status': 'success',
                    'message': f'Welcome back, {user.username}!',
                    'redirect_url': reverse("main:show_name")
                }
                response = JsonResponse(response_data, status=200)
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
           
            response_target.set_cookie('last_login', str(datetime.datetime.now()))
            return response_target
            
        else:
            
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                errors = dict(form.errors.items())
                return JsonResponse({
                    'status': 'error', 
                    'message': 'Login gagal!.', 
                    'errors': errors
                }, status=400)
           
            
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        response = JsonResponse({
            'status': 'success', 
            'message': 'You have been logged out successfully.'
        }, status=200)
        response.delete_cookie('last_login')
        return response


    
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def add_employee(request):
    emp = employee.objects.create(name="daniel",age="18",persona="mahasiswa sistem informasi")
    context ={
        'employee' : emp
    }
    return render(request,'employee.html', context)

@login_required(login_url='/login')
@csrf_exempt
def edit_product_ajax(request, pk):
    try: 
        product = Product.objects.get(pk=pk, user=request.user)
    except Product.DoesNotExist:
        return JsonResponse({'status' : 'error', 'message': ' Product tidak ditemukan'},status=404)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': f'Product "{product.name}" berhasil diupdate'}, status=200)
        else:
            errors = dict(form.errors.items())
            return JsonResponse({'status': 'error', 'message': 'Product gagal diupdate', 'errors': errors}, status=400)

    return JsonResponse({ 
    'id': product.pk, 
    'name': product.name, 
    'price': product.price, 
    'description': product.description,
    'category': product.category, 
    'thumbnail': product.thumbnail, 
    'is_featured': product.is_featured, 
})

@login_required(login_url='/login')
@csrf_exempt
@require_http_methods(["DELETE", "POST"])
def delete_product_ajax(request, pk): 
    try:
        product = Product.objects.get(pk=pk, user=request.user) 
    except Product.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Product tidak ditemukan'}, status=404)
    
    # Logika tetap sama
    if request.method == 'DELETE' or request.POST.get('_method') == 'DELETE':
        product.delete()
        return JsonResponse({'status': 'success', 'message': f'Product "{product.name}" telah dihapus'}, status=200)   
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

@csrf_exempt
@require_POST
@login_required(login_url='/login')
def add_product_entry_ajax(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  
    user = request.user
    
    new_product = Product(
        name=name,
        price=price,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)



    


