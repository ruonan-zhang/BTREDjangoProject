from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'pages/index.html') #render takes in template_name and look for that file in template

def about(request):
	return render(request, 'pages/about.html')
