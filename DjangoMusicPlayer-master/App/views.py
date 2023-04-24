from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .models import CustomUser, MusicFile
from django.db.models import Q

@login_required
def home(request):
    user = request.user
    music_files = MusicFile.objects.filter(Q(file_type='public') | Q(allowed_users=user))
    return render(request, 'home.html', {'music_files': music_files})
@login_required
def upload(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        file_type = request.POST.get('file_type')
        file = request.FILES.get('file')

        if not title or not file_type or not file:
            messages.error(request, 'Please fill all the fields.')
            return redirect('upload')

        music_file = MusicFile(title=title, file=file, file_type=file_type)
        music_file.save()

        if file_type == 'protected':
            allowed_users = request.POST.getlist('allowed_users')
            for email in allowed_users:
                try:
                    user = CustomUser.objects.get(email=email)
                    music_file.allowed_users.add(user)
                except CustomUser.DoesNotExist:
                    pass

        messages.success(request, 'Music file uploaded successfully.')
        return redirect('home')

    return render(request, 'upload.html')
def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, 'Please fill all the fields.')
            return redirect('register')

        user = CustomUser.objects.create_user(email=email, password=password)
        user.save()

        messages.success(request, 'Account created successfully.')
        return redirect('login')

    return render(request, 'register.html')
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, 'Please fill all the fields.')
            return redirect('login')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('login')

    return render(request, 'login.html')
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('login')

