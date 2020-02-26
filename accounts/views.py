from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')


def signup(request):

    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['Username'])
                return render(request, 'accounts/signup.html', {'message': 'User Already Exists'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['Username'], password=request.POST['password1'])
                #auth.login(request, user)
                return render(request, 'accounts/signup.html',{'message': 'User Registration Successful'})
        else:
            return render(request, 'accounts/signup.html', {'message': 'Passwords Does Not Match'})

    else: 
        return render(request, 'accounts/signup.html')

def login(request):

    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['Username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return render(request, 'accounts/welcome.html', {'username':request.POST['Username']})
        else:
            return render(request, 'accounts/login.html', {'message': 'Username or Password is incorrect'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'accounts/signup.html')













