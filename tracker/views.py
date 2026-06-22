from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Skill


# HOME
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    skills = Skill.objects.filter(user=request.user)

    total = skills.count()

    return render(request, "tracker/home.html", {
        "skills": skills,
        "total": total
    })


# ADD SKILL
def add_skill(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        Skill.objects.create(
            user=request.user,
            name=request.POST['name'],
            category=request.POST['category'],
            level=request.POST['level'],
            progress=request.POST['progress']
        )
        return redirect('/')

    return render(request, "tracker/add_skill.html")


# DELETE SKILL
def delete_skill(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    skill = Skill.objects.get(id=pk, user=request.user)

    if request.method == "POST":
        skill.delete()
        return redirect('/')

    return render(request, "tracker/delete_skill.html", {
        "skill": skill
    })


# LOGIN
def login_view(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid login")

    return render(request, "auth/login.html")


# REGISTER
def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists")
        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return redirect('/login/')

    return render(request, "auth/register.html")


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('/login/')