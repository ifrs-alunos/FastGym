from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from . import forms, models

def home(request):
	return render(request, "clients/home.html", {})

def login_user(request):
	if request.method == "POST":
		user_form = forms.MyAutenticationForm(request, request.POST)
		print("\n\nÉ POST\n\n")
		if user_form.is_valid():
			print("\n\nÉ VÁLIDO\n\n")
			user = user_form.get_user()
			login(request, user)
			return redirect("home")
	else:
		user_form = forms.MyAutenticationForm(request.POST)
	print("\n\nDEVOLVIDA PÁGINA DE LOGIN\n\n")
	return render(request, "clients/login.html", {'page_title':'Login', 'form':user_form})

def cadastro(request):
	if request.method=="POST":
		user_form = forms.MyUserCreationForm(request.POST)
		data_form = forms.CadastroFisicoForm(request.POST)
		if user_form.is_valid() and data_form.is_valid():
			user = user_form.save()
			profile = data_form.save(commit=False)
			profile.owner = user
			profile.save()

			login(request, user)
			messages.success(request, "Cadastro realizado com sucesso. Seja bem-vindo")
			return redirect("home")
	else:
		user_form = forms.MyUserCreationForm()
		data_form = forms.CadastroFisicoForm()
	return render(request, "clients/cadastro-usuario.html", {'page_title':'Cadastro', 'form_user': user_form,'form_dados':data_form})
