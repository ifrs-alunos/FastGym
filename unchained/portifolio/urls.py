from django.urls import path
from .views import gym_view

app_name = "portfolio"

urlpatterns = [
     path('<int:gym_id>/', gym_view, name="gym_view")
]