from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='login'),
    path('login/', views.login, name='login')
]
