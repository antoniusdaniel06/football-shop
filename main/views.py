from django.shortcuts import render

# Create your views here.
def show_name(request):
    person = {
        'name' :'Antonius Daniel',
        'npm' : '2406496012',
        'class' : 'PBP E'
    }
    return render(request, "main.html", person)
