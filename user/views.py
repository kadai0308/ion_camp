from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from user.models import Profile
import datetime


def login(request):
    return render(request, 'user/login.html')


def loginAuth(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password = password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return redirect('/')
    else:
        return redirect('/login')


def logout(request):
    auth.logout(request)
    return redirect('/')


def signup(request):
    return render(request, 'user/signup.html')


def create(request):
    print(request.POST.get('password', ''))
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    name = request.POST.get('name', '')

    new_user = User.objects.create_user(email, email, password)

    sex = (request.POST.get('sex', '') == '男') and 'male' or 'female'
    birthday = request.POST.get('birthday', '')
    birthday = datetime.datetime.strptime(birthday, '%Y/%m/%d')
    taiwanId = request.POST.get('taiwanId', '')
    vegetarian = (request.POST.get('vegetarian', '') == '素') and True or False
    contactPerson = request.POST.get('contactPerson', '')
    guardian = request.POST.get('guardian', '')
    address = request.POST.get('address', '')
    phone = request.POST.get('phone', '')
    ojAccount = request.POST.get('ojAccount', '')
    selfIntro = request.POST.get('selfIntro', '')
    joinReason = request.POST.get('joinReason', '')

    Profile.objects.create(
        user = new_user,
        name = name,
        sex = sex,
        birthday = birthday,
        taiwanId = taiwanId,
        vegetarian = vegetarian,
        contactPerson = contactPerson,
        guardian = guardian,
        address = address,
        phone = phone,
        ojAccount = ojAccount,
        selfIntro = selfIntro,
        joinReason = joinReason,
    )

    return redirect('/')
