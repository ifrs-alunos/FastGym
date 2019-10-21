from django.shortcuts import render

def index(request):
	context = {}
	return renser(request, 'base.html', context)