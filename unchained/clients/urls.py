from django.urls import path, include
from .views import base, login

urlpatterns = [
	path('', base, name="base"),
	path('login/', login, name="login")
]