from django.shortcuts import render

def cadastro(request):
	context = {}
	return render(request, 'cadastro_usuario/cadastro.html', context)
