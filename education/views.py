from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Davomat, Homework
from .forms import DavomatForm, HomeworkForm

@login_required
def home(request):
    davomatlar = Davomat.objects.all().order_by('-sana')
    homeworks = Homework.objects.all().order_by('-sana')  # Homework ro‘yxatini qo‘shish
    return render(request, 'education/home.html', {'davomatlar': davomatlar, 'homeworks': homeworks})

@login_required
def davomat_qoshish(request):
    if request.method == 'POST':
        form = DavomatForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Davomat muvaffaqiyatli qo‘shildi!")
            return redirect('education:home')
        else:
            messages.error(request, "Xatolik yuz berdi. Iltimos, ma’lumotlarni tekshiring.")
    else:
        form = DavomatForm()
    return render(request, 'education/davomat_qoshish.html', {'form': form})

@login_required
def homework_qoshish(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Homework muvaffaqiyatli qo‘shildi!")
            return redirect('education:home')
        else:
            messages.error(request, "Xatolik yuz berdi. Iltimos, ma’lumotlarni tekshiring.")
    else:
        form = HomeworkForm()
    return render(request, 'education/homework_qoshish.html', {'form': form})

@login_required
def about(request):
    return render(request, 'education/about.html', {'title': 'About'})