from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from models import User
from .models import User, Tourdate
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
def logout(request):
    del request.session['theuser']
    del request.session['userid']
    return redirect('/logpage')
def dashboard(request):
		# tourdatetime = Tourdate.tourdatetime
		# tourcity = Tourdate.tourcity
		# tourvenue = Tourdate.tourvenue
		# tourinfourl = tourinfourl
	tourdateall = Tourdate.objects.all()
	context={
		'tourdateall': tourdateall,
	}
	return render(request, "login_app/tourdates.html", context)
def add(request):
	if request.method == 'POST':
		tourdateall = Tourdate.objects.addtourdate(request.POST)
		if 'errors' in tourdateall:
			for error in tourdateall['errors']:
				messages.error(request, error)
			return redirect ('/dashboard')
		if 'Tourdateid' in tourdateall:
			return redirect('/dashboard')
def delete(request):
	# tourdaterow = Tourdate.objects.get(id=id)
	# context = {
	# 	'tourdaterow':tourdaterow
	# }
	# tourdaterow.delete()
	return redirect('/dashboard')
