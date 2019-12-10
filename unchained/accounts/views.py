from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from . import forms

def home(request):
	return render(request, "accounts/home.html", {})

def login_user(request):
	if request.method == "POST":
		user_form = forms.MyAutenticationForm(request, request.POST)
		if user_form.is_valid():
			user = user_form.get_user()
			login(request, user)
			return redirect("home")
	else:
		user_form = forms.MyAutenticationForm(request.POST)
	return render(request, "accounts/login.html", {'page_title': 'Login', 'form':user_form})

def register_user(request):
	if request.method=="POST":
		user_form = forms.MyUserCreationForm(request.POST)
		data_form = forms.PersonalProfileRegisterForm(request.POST)
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
		data_form = forms.PersonalProfileRegisterForm()
	return render(request, "accounts/cadastro-usuario.html", {'page_title': 'Cadastro', 'form_user': user_form, 'form_dados':data_form, 'formto':'accounts:register_user'})

def register_gym(request):
	if request.method=="POST":
		user_form = forms.MyGymUserCreationForm(request.POST)
		data_form = forms.GymProfileRegisterForm(request.POST)
		if user_form.is_valid() and data_form.is_valid():
			user = user_form.save()
			profile = data_form.save(commit=False)
			profile.owner = user
			profile.save()

			login(request, user)
			messages.success(request, "Cadastro realizado com sucesso. Seja bem-vindo")
			return redirect("home")
	else:
		user_form = forms.MyGymUserCreationForm()
		data_form = forms.GymProfileRegisterForm()
	return render(request, "accounts/cadastro-usuario.html", {'page_title': 'Cadastro', 'form_user': user_form, 'form_dados':data_form, 'formto':'accounts:register_gym'})
