from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html')

def addUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']

        # Check if passwords match
        if password == re_password:
            # Check if username or email already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('/signup/')
            elif User.objects.filter(email=email).exists():  # Fixed exists() call
                messages.error(request, 'Email already exists.')
                return redirect('/signup/')
            else:
                # Create the user if no duplicates are found
                user = User.objects.create_user(
                    username=username,
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    password=password
                )
                user.save()
                messages.success(request, 'Registration successful.')
                return redirect('/login/')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('/signup/')
    else:
        return redirect('/signup/')

def login(request):
    return render(request, 'login.html')

def loginForm(request):
    if request.method == 'POST':
        username = request.POST['username']  # Corrected from request.Post to request.POST
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')
    else:
        return redirect('login')

def logout(request):
    auth.logout(request)
    return redirect('login')
