from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from .forms import SignUp


# Create your views here.
@csrf_exempt
def register(request):
    if request.method == "POST":

        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_auth:login')
    else:
        form=SignUp()
    form = SignUp()
    return render(request, 'authentication/register.html', {'form':form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('snetech:home')
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form':form})



def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:show_user')
        )
    
def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })

def user_logout(request):
    logout(request)
    return redirect('snetech:home')