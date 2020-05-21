#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse('Hello, World!!')
    
    return render(request, 'index.html')

''' 
   texts = ['Esse é um site sobre', 'Django', 'Você sabe o que é', 'Django?']
    
    context = {
        'title':'Django E-Commerce',
        'texts': texts
    }

    return render(request, 'index.html', context) #procura o arquivo index.html dentro do diretório core/templates 
'''
    

def base(request):
      
    return render(request, 'base.html')

def contact(request):
      
    return render(request, 'contact.html')

def product(request):
      
    return render(request, 'product.html')

def product_list(request):
      
    return render(request, 'product_list.html')

def warning(request):
    
    return render(request, 'warning.html')

def about(request):
    
    return render(request, 'about.html')