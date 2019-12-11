from django.urls import path
from .views import gym_view, gym_search, register_product

app_name = "portfolio"

urlpatterns = [
     path('<int:gym_id>/', gym_view, name="gym_view"),
     path('pesquisa/', gym_search, name="gym_search"),
     path('cadastro-produto', register_product, name="register_product"),
]