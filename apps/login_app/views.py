from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from models import User
# Create your views here.
# views.py
def index(request):
	return render(request, "login_app/index.html")
def register(request):
    if request.method=="POST":
        user = User.objects.register(request.POST)
    if 'errors' in user:
        for error in user['errors']:
            messages.error(request, error)
        return redirect('/')
    if 'theuser' in user:
        request.session['theuser'] = user['theuser']
        request.session['userid'] = user['userid']
        return redirect('/dashboard')
def login(request):
    if request.method =="POST":
        user = User.objects.login(request.POST)
        if 'errors' in user:
            for error in user['errors']:
                messages.error(request, error)
                return redirect('/')
        if 'theuser' in user:
            request.session['theuser'] = user['theuser']
            request.session['userid'] = user['userid']
            return redirect('/dashboard')
def logpage(request):
	return render(request, "login_app/login.html")
def dashboard(request):
	request.session['username'] = request.POST['username']
	return render(request, "login_app/tourdates.html")
