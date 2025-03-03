from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

# Registration API

@csrf_exempt
@api_view(['POST'])
def api_signup(request):
    if request.method == 'POST':
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not email or not password:
            return JsonResponse({"message": "All fields are required"}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"message": "Username already exists"}, status=400)

        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()
        return JsonResponse({"message": "User registered successfully"}, status=201)

@csrf_exempt  # Disable CSRF protection for this view
@api_view(['POST'])
def api_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return JsonResponse({"message": "Username and password are required"}, status=400)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Login successful"}, status=200)
        else:
            return JsonResponse({"message": "Invalid credentials"}, status=401)

# Logout API
@csrf_exempt
@api_view(['POST'])
def api_logout(request):
    if request.method == 'POST':
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
