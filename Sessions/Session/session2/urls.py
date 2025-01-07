from django.contrib import admin  
from django.urls import path  
from . import views  

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('ssession/', views.setsession),  # Added trailing slash for consistency
    path('gsession/', views.getsession),  
]
