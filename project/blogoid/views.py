from django.shortcuts import render

def home(request):
	return render(request, 'blogoid/home.html')

def about(request):
	return render(request, 'blogoid/about.html')	