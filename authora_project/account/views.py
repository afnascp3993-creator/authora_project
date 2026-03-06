from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserRegistration
from dashboard.views import user_dashboard,admin_dashboard

@login_required
def login_view(request):
    return render(request, "login.html")

def login(request):
    if request.method == "POST":
        print("12")
        username = request.POST.get("username")
        password = request.POST.get("password")

        

        user=UserRegistration.objects.get(username=username,password=password)
        request.session['userId']=user.id
        

        # user = authenticate(request, username=username, password=password)
        if user.roles == 'admin':
            return redirect(admin_dashboard)
        elif user.roles == 'user':
            return redirect(user_dashboard)
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        if not all([username, email, phone, password, password_confirm]):
            messages.error(request, "All fields are required")
            return redirect("register")

        if password != password_confirm:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if UserRegistration.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        if UserRegistration.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("register")

        if UserRegistration.objects.filter(phone=phone).exists():
            messages.error(request, "Phone already exists")
            return redirect("register")

        UserRegistration.objects.create(
            username=username,
            email=email,
            phone=phone,
            password=password,
            roles="user",
        )

        messages.success(request, "Registration Successful")
        return redirect("login")

    return render(request, "register.html")


def create_user_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        password = request.POST.get("password", "").strip()
        role = request.POST.get("role", "user")

        if not all([username, email, phone, password]):
            messages.error(request, "All fields are required.")
            return redirect("create_user")

        if UserRegistration.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("create_user")

        if UserRegistration.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("create_user")

        UserRegistration.objects.create(
            username=username,
            email=email,
            phone=phone,
            password=password,
            roles=role,
        )
        messages.success(request, f"User '{username}' created successfully!")
        return redirect("create_user")

    users = UserRegistration.objects.all().order_by("-id")
    return render(request, "create_user.html", {"users": users})