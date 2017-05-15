from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user.models import Profile


def index(request):
    application = Profile.objects.all()
    return render(request, 'management/index.html', locals())


def passApply(request, apply_id):
    application = Profile.objects.get(id=apply_id)
    application.state = 'pass'
    application.save()
    return redirect('/management')


def rejectApply(request, apply_id):
    application = Profile.objects.get(id=apply_id)
    application.state = 'reject'
    application.save()
    return redirect('/management')
