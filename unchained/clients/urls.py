from django.urls import path, include
from .views import login, cadastro

urlpatterns = [
	path('login/', login, name="login"),
	path('cadastro/', cadastro, name="cadastro")
]