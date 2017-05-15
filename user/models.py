from django.db import models
from django.contrib.auth.models import User


class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    birthday = models.DateTimeField()
    taiwanId = models.CharField(max_length=255)
    vegetarian = models.BooleanField(default=False)
    contactPerson = models.CharField(max_length=255)
    guardian = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    ojAccount = models.TextField()
    selfIntro = models.TextField()
    joinReason = models.TextField()
    state = models.CharField(max_length=255, default='WaitForCheck')
