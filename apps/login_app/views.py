from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from models import User
from .models import User, Tourdate, Subscriber
from datetime import date, datetime
# Create your views here.
# views.py
def index(request):
	now = datetime.now()
	tourdateall = Tourdate.objects.order_by('tourdatetime')
	context={
		'tourdateall': tourdateall,
	}
	return render(request, "login_app/index.html", context)
def thankyouPage(request):
	newSubscriber = Subscriber.objects.order_by('-created_at')
	context={
		'newSubscriber': newSubscriber,
	}
	return render(request, "login_app/thankyou.html", context)
def addsubscriber(request):
		if request.method == 'POST':
			newSubscriber = Subscriber.objects.addSubscriber(request.POST)
			if 'errors' in newSubscriber:
				for error in newSubscriber['errors']:
					messages.error(request, error)
				return redirect ('/')
			if 'subscriberID' in newSubscriber:
				return redirect('/thankyou')
def register(request):
    if request.method=="POST":
        user = User.objects.register(request.POST)
    if 'errors' in user:
        for error in user['errors']:
            messages.error(request, error)
        return redirect('/logpage')
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
	try:
		request.session['theuser']
	except KeyError:
		return redirect('/')
	tourdateall = Tourdate.objects.order_by('-tourdatetime')
	# tourdateall = Tourdate.objects.all()
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
def deleteview(request, id):
	Tourdate.objects.deletetourdate(id=id)
	# print id
	return redirect('/dashboard')
