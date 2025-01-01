from django.contrib import admin
from .models import Customer
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'unique_id')  # Show unique ID
    search_fields = ('username', 'email', 'unique_id')  # Enable search by unique ID
