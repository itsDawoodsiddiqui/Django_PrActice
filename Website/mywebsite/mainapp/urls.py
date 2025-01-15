from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('home1/', views.home1, name='home1'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
]

