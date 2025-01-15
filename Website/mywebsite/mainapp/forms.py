from django import forms
from .models import  User  # Import your custom User model
from django.forms import ModelForm

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'message']  # Use fields from your custom User model
        widgets = {
            'email': forms.EmailInput(),
            'message': forms.Textarea(attrs={'rows': 4}),
        }




class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()


from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'password']
