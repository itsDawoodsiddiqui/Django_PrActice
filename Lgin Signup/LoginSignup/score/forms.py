from django.forms import ModelForm
from .models import Customer
from django import forms


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class LoginForm(forms.Form):  # New form for login
    email = forms.EmailField(max_length=150)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


