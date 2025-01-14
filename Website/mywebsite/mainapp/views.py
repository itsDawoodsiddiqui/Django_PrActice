from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from .forms import ProfileForm

def home(request):

    # username = request.session.get('username', None)
    # if username:
    #     return render(request, 'index.html', {'username': username})
    # else:
    #     return redirect('login')


# # In dono main say koi ik code chalay ga


    username = request.session.get('username', None) 
    if username:
        return render(request, 'index.html', {'username': username})
    else:
        return redirect('login')  


def home1(request):
    return HttpResponse("HelloWorld")


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)  
            request.session['username'] = user.name
            return redirect('home')  
    else:
        form = SignupForm()
    return render(request, 'contact.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                request.session['username'] = user.username  # Store the username in session
                return redirect('home')  # Redirect to home page
            except User.DoesNotExist:
                messages.error(request, 'Invalid email address.')
                return redirect('login')  
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            request.session['username'] = user.username  # Save username in session
            return redirect('home')  # Redirect to home page
        else:
            messages.error(request, "Signup failed. Please correct the errors.")
    else:
        form = ProfileForm()
    return render(request, 'signup1.html', {'form': form})
