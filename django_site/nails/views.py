from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserLoginForm, UserRegisterForm, UsersUpdateForm


def index(request):
    return render(request, 'nails/index.html')


def courses(request):
    return render(request, 'nails/courses.html', {'courses': Course.objects.filter(show=True)})


def log_in(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'nails/login.html', {'form': form})


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if user.username[:2] not in '89':
                messages.error(request, 'Неверный номер телефона!')
                return render(request, 'nails/registration.html', {'form': form})
            user.telephone = user.username
            user.role = Role.objects.get(name='Клиент')
            user.save()
            login(request, user)
            return redirect('profile', user.pk)
    else:
        form = UserRegisterForm()
    return render(request, 'nails/registration.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login')
def enroll(request, pk_user, pk_timesheet):
    timesheet = Timesheet.objects.get(pk=pk_timesheet)
    user = User.objects.get(pk=pk_user)
    if timesheet.quantity > 0:
        try:
            Request.objects.get(user=user, timesheet=timesheet)
            messages.error(request, 'Вы уже записаны!')
        except:
            timesheet.quantity = timesheet.quantity - 1
            Request.objects.create(user=user,
                                   timesheet=timesheet,
                                   status=Status.objects.get(name='Не рассмотрено'))
            timesheet.save()
    else:
        messages.error(request, 'Места закончились!')
    return redirect('profile', pk_user)


@login_required(login_url='login')
def delete_enroll(request, pk_user, pk_request):
    req = Request.objects.get(pk=pk_request)
    timesheet = req.timesheet
    timesheet.quantity = timesheet.quantity + 1
    timesheet.save()
    req.delete()
    return redirect('profile', pk_user)


@login_required(login_url='login')
def profile(request, pk):
    if request.user.pk != pk:
        return redirect('profile', request.user.pk)
    instance = get_object_or_404(User, pk=pk)
    form = UsersUpdateForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Успешно изменено!')
            return redirect('profile', pk)
        else:
            messages.error(request, 'Некорректные данные!')
    return render(request, 'nails/profile.html', {'form': form, 'timesheet': Timesheet.objects.all(),
                                                  'my_courses': Request.objects.filter(user=User.objects.get(pk=pk))})
