from django.shortcuts import render
from main.models import Tutorial
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def contact(request):
	return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def myprojects(request):
    return render(request=request, 
                  template_name='myprojects.html',
                  context={"tutorials": Tutorial.objects.all})

def about(request):
    return render(request, 'about.html')

@csrf_exempt
def contact(request):
    #if post request came 
    if request.method == 'POST':
        #getting values from post
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
 
        #adding the values in a context variable 
        context = {
            'name': name,
            'email': email,
            'phone': phone
        }
        
        #getting our showdata template
        template = loader.get_template('showdata.html')

        return redirect("main:homepage")

    else:
        #if post request is not true 
        #returing the form template 
        template = loader.get_template('contact.html')
        return HttpResponse(template.render())