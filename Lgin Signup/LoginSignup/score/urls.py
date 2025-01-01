from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('customers/', views.customer_list, name='customer_list'),  # Naya view
]

