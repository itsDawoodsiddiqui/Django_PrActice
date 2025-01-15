from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm, ProfileForm

def home(request):
    # """Handle the home page."""
    # username = request.session.get('username', None)  # Check if username exists in session
    # if username:
    #     return render(request, 'index.html', {'username': username})
    # else:
    #     # Display a warning message if the user is not logged in
    #     messages.warning(request, "You are not logged in. Some features may be unavailable.")
    #     return render(request, 'index.html', {'username': None})

    username = request.session.get('username', None)
    if username:
        return render(request, 'index.html', {'username': username})
    messages.warning(request, "You are not logged in. Some features may be unavailable.")
    return render(request, 'index.html', {'username': username})
    
    
    
def home1(request):
    return HttpResponse("HelloWorld")
    
    
def about(request):
    """Render the about page."""
    return render(request, "about.html")

def contact(request):
    """Handle the contact form submission."""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['username'] = user.name  # Use 'name' instead of 'username'
            return render(request, 'index.html', {'username': user.name})
        else:
            messages.error(request, "Signup failed. Please correct the errors.")
    else:
        form = SignupForm()
    return render(request, 'contact.html', {'form': form})


def login_view(request):
    """Handle user login."""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)  # Retrieve user by email
                auth_user = authenticate(username=user.username, password=password)
                if auth_user is not None:
                    login(request, auth_user)  # Log the user in
                    request.session['username'] = auth_user.username  # Save username in session
                    return render(request, 'index.html', {'username': auth_user.username})
                else:
                    messages.error(request, 'Invalid password. Please try again.')
            except User.DoesNotExist:
                messages.error(request, 'No user found with this email.')
        else:
            messages.error(request, 'Invalid form input. Please try again.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def signup(request):
    """Handle user signup."""
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user profile
            request.session['username'] = user.username  # Save username in session
            return render(request, 'index.html', {'username': user.username})
        else:
            messages.error(request, "Signup failed. Please correct the errors.")
    else:
        form = ProfileForm()

    return render(request, 'signup1.html', {'form': form})
