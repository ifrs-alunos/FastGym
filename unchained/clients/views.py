from django.shortcuts import render


def base(request):
	return render(request, "clients/base.html", {})

def login(request):
	return render(request, "clients/login.html", {})

#def base(request):
#	return render(request, "clients/base.html", {})

#def base(request):
#	return render(request, "clients/base.html", {})
