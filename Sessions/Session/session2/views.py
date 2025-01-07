from django.shortcuts import render  
from django.http import HttpResponse 
from django.contrib.sessions.models import Session

def setsession(request):  
    request.session['sname'] = 'Irfan'  
    request.session['semail'] = 'irfan.sssit@gmail.com'  
    return HttpResponse("Session is set successfully!")  

def getsession(request):  
    # Use `.get()` to avoid errors if the session key doesn't exist
    studentname = request.session.get('sname', 'Guest')  
    studentemail = request.session.get('semail', 'No Email')  
    return HttpResponse(f"Name: {studentname}, Email: {studentemail}")  



