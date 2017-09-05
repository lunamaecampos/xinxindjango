from django.shortcuts import render

# Create your views here.
# views.py
def index(request):
	return render(request, "login_app/index.html")

def logpage(request):
	return render(request, "login_app/login.html")
def dashboard(request):
	return render(request, "login_app/tourdates.html")
