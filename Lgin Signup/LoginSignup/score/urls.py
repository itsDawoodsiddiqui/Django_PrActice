from django.urls import path
from . import views

urlpatterns = [
    
    path('login/', views.login, name='login'),
    path('customers/', views.customer_list, name='customer_list'),  # Naya view
    path('home1/', views.home1, name='home1'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),   
]

