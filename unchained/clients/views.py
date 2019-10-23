from django.shortcuts import render

def base(request):
	return render(request, "clients/base.html", {})

def login(request):
	return render(request, "clients/login.html", {'page_title':'Login'})

def cadastro(request):
	print(request.method)
	if request.method=="POST":
		return render(request, "clients/login.html", {'page_title':'Login'})
	return render(request, "clients/cadastro.html", {'page_title':'Cadastro'})

#def base(request):
#	return render(request, "clients/base.html", {})

#def base(request):
#	return render(request, "clients/base.html", {})
