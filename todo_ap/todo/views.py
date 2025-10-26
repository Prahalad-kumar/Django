from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import Todo


# Dashboard / Home
def home(request):
    if not request.user.is_authenticated:
        return redirect('login_view')
    tasks = Todo.objects.filter(user=request.user).order_by('-srno')
    return render(request, 'home.html', {'tasks': tasks})


# Signup
def signup(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'signup.html')

        if User.objects.filter(username=fullname).exists():
            messages.error(request, "Username already exists!")
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return render(request, 'signup.html')

        user = User.objects.create_user(username=fullname, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login_view')

    return render(request, 'signup.html')


# Login (email-based)
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            username = User.objects.get(email=email).username
            user = authenticate(request, username=username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password!")
            return render(request, 'login.html')

    return render(request, 'login.html')


# Logout
def logout_view(request):
    auth_logout(request)
    return redirect('login_view')


# Add Task
def add_task(request):
    if request.method == 'POST' and request.user.is_authenticated:
        task_text = request.POST.get('task_text')
        if task_text:
            Todo.objects.create(user=request.user, title=task_text)
    return redirect('home')


# Toggle Task Completion
def toggle_task(request, srno):
    task = get_object_or_404(Todo, srno=srno, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('home')


# Edit Task
def edit_task(request, srno):
    task = get_object_or_404(Todo, srno=srno, user=request.user)
    if request.method == 'POST':
        new_text = request.POST.get('task_text')
        if new_text:
            task.title = new_text
            task.save()
            return redirect('home')
    return render(request, 'edit_task.html', {'task': task})


# Delete Task
def delete_task(request, srno):
    task = get_object_or_404(Todo, srno=srno, user=request.user)
    task.delete()
    return redirect('home')
