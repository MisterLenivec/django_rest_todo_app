from django.urls import path
from . import views


urlpatterns = [
    path('', views.front_list, name='list'),
]