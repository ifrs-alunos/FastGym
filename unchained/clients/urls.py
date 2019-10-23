from django.urls import path, include
from .views import base, login, cadastro

urlpatterns = [
	path('', base, name="base"),
	path('login/', login, name="login"),
	path('cadastro/', cadastro, name="cadastro")
]