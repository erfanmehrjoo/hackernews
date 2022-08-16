from django.shortcuts import render , redirect 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login , authenticate , logout
from .forms import LinkForm , UserForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def login_custom(request):
    form = 'login'
    if request.user.is_authenticated:
        return redirect("admin:index")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request , "User not found")
            return redirect("login")
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect("admin:index")
    return render(request , 'login.html' , context={form : "login"})

def logout_custom(request):
    logout(request)
    return redirect("login")

def register_custom(request):
    pass