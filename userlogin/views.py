from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        username = request.POST['id_username']
        password = request.POST['id_password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('helloworld/home')
        message.success(request, "There was an issue logging in")
        return redirect('login')
    else:
        return render(request, 'registration/login.html')
