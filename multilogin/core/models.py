"""
Definition of models.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm


class Employee(AbstractUser):

    qr_code = models.CharField(
        max_length=100,
    )

    token = models.CharField(
        max_length=100,
        default="NULL",
    )

    def __str__(self):
        return self.username

    @property
    def QR_Generator(self):
        return str(self.username) + str(self.password)


class LoginForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['username', 'password']


class PartsDataUser(models.Model):

    name = models.CharField(
        'Username',
        max_length=50,
        unique=True,
    )

    user = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,

    )

    password = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.name


class SmartControlUser(models.Model):

    name = models.CharField(
        'Username',
        max_length=50,
    )

    password = models.CharField(
        max_length=50,
    )

    token = models.CharField(
        max_length=32,
        null=True,
    )

    last_login = models.DateTimeField(
        null=True,
    )

    due_date = models.DateTimeField(
        null=True,
    )

    user = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        null=True,

    )

    def __str__(self):
        return self.name


class BinManagerUser(models.Model):

    name = models.CharField(
        'Username',
        max_length=50,
    )

    password = models.CharField(
        max_length=50,
    )

    token = models.CharField(
        max_length=32,
        null=True,
    )

    surname = models.CharField(
        max_length=50,
    )

    email = models.CharField(
        max_length=50,
    )

    department_id = models.IntegerField(
    )

    position = models.IntegerField(
    )

    is_root = models.BooleanField(
    )

    is_firstuse = models.BooleanField(
    )

    is_active = models.BooleanField(
    )

    def __str__(self):
        return self.name


class Website(models.Model):

    name = models.CharField(
        max_length=50,
        unique=True,
    )

    url = models.CharField(
        max_length=50,
        unique=True,
    )

    def __str__(self):
        return self.name
