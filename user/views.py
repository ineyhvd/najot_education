from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser

def auth_view(request):
    login_form = LoginForm()
    register_form = RegisterForm()

    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                if CustomUser.objects.filter(username=username).exists():
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        messages.success(request, "Xush kelibsiz!")
                        return redirect('education:home')  # education:home ga o‘tadi
                    else:
                        messages.error(request, "Parol noto'g'ri!")
                else:
                    messages.error(request, "Bu username ro'yxatdan o'tmagan!")

        elif 'register' in request.POST:
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                user = register_form.save(commit=False)
                user.set_password(register_form.cleaned_data['password'])
                user.save()
                login(request, user)
                messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz!")
                return redirect('education:home')  # education:home ga o‘tadi

    return render(request, 'user/auth.html', {
        'login_form': login_form,
        'register_form': register_form
    })

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Tizimdan chiqdingiz!")
    return redirect('user:auth')