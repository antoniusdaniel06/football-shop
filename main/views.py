from django.shortcuts import get_object_or_404, redirect, render
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_name(request):
    person = {
        'App_name' : "BluR Sport",
        'name' :'Antonius Daniel',
        'npm' : '2406496012',
        'class' : 'PBP E'
    }
    return render(request, "main.html", person)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('product_list')

    context = {"form" : form}
    return render(request,"form.html",context)

def product_list(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request,'product_list.html',context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "detail.html", {"product": product})

def show_xml(request):
    products = Product.objects.all()
    xml_data = serializers.serialize("xml" , products)
    return HttpResponse(xml_data, content_type="application/xml")

def show_xml_by_id(request, news_id):
   try:
       product = Product.objects.filter(pk=news_id)
       xml_data = serializers.serialize("xml", product)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json(request):
    products = Product.objects.all()
    json_data = serializers.serialize('json', products)
    return HttpResponse(json_data, content_type="application/json")

def show_json_by_id(request, news_id):
   try:
       product = Product.objects.filter(pk=news_id)
       json_data = serializers.serialize("json", product)
       return HttpResponse(json_data, content_type="application/json")
   except Product.DoesNotExist:
       return HttpResponse(status=404)




