from django.urls import path
from .views import login_user, register_user, register_gym, logout_user
app_name = "accounts"
urlpatterns = [
	path('login/', login_user, name="login"),
	path('cadastro/', register_user, name="register_user"),
	path('cadastro-academia/', register_gym, name="register_gym"),
	path('logout/', logout_user, name="logout")
]