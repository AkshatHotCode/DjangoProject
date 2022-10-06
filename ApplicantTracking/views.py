from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "ApplicantTracking/index.html")


def signup(request):
    if request.method == "POST":
        # username = request.POST.get('username')
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some another username")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "email already exist!")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Password didn't match")

        myuser = User.objects.create_user(username, email, pass1)
        myuser.name = name

        myuser.save()

        messages.success(request, "Your account has been successfully created")

        return redirect('signin')

    return render(request, "ApplicantTracking/signup.html")


def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            # name = user.name
            return render(request, "ApplicantTracking/index.html")

        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')

    return render(request, "ApplicantTracking/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')