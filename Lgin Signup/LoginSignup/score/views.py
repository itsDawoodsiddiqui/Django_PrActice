from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Customer
from django.contrib.auth.hashers import make_password
from .forms import CustomerForm, LoginForm
from django.core.paginator import Paginator
from .utils import *
from .models import uuid
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return render(request, 'score/index.html')

        # Check if username or email already exists in Customer model
        if Customer.objects.filter(username=username).exists() or Customer.objects.filter(email=email).exists():
            messages.error(request, "Username or email already taken.")
        else:
            # Hash the password before saving it to the database
            hashed_password = make_password(password)
            # Create and save the customer
            customer = Customer(username=username, email=email, password=hashed_password)
            customer.save()
            messages.success(request, "Signup successful!")
            return redirect('home1/')  # Redirect to login  page

        return render(request, 'score/index.html')

    return render(request, 'score/index.html')





def customer_list(request):
    customers = Customer.objects.all()  # Sare customers ko query karna
    paginator = Paginator(customers, 5)  # Har page par 5 customers dikhana

    page_number = request.GET.get('page')  # Query parameter se page number lena
    page_obj = paginator.get_page(page_number)  # Current page ka data

    return render(request, 'score/customer_list.html', {'page_obj': page_obj})



# Login View
def login(request):
    form = LoginForm()  # Create an instance of the form
    if request.method == 'POST':
        form = LoginForm(request.POST)  # Populate the form with POST data
        if form.is_valid():  # Validate the form
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Welcome to the Todo App")
                return redirect('home1/')
            else:
                messages.error(request, "Invalid email or password.")
                # Debugging: print the failed login attempt
                print(f"Failed login attempt for email: {email}")
    return render(request, 'score/login.html', {'form': form})
 


# Add Customer View
def add_customer(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomerForm(request.POST)
            if form.is_valid():
                form.save()  # Save the customer data
                messages.success(request, "Customer added successfully!")
                return redirect('add_customer')  # Redirect to the same page or another one
            else:
                messages.error(request, "Error saving customer. Please try again.")
        else:
            form = CustomerForm()  # Empty form for GET request

        return render(request, 'score/add_customer.html', {'form': form})
    else:
        messages.error(request, "You must be logged in to add a customer.")
        return redirect('login')



def home(request):
    return render(request, 'home.html')


def home1(request):
    return HttpResponse("HelloWorld")


def about(request):
    return HttpResponse("About Us")

def contact(request):
    return HttpResponse("Contact us")