from django.urls import path
from .views import login_user, cadastro
app_name = "clients"
urlpatterns = [
	path('login/', login_user, name="login"),
	path('cadastro/', cadastro, name="cadastro")
]