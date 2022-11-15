from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .models import *
from .serializers import *


@login_required(login_url='login/')
def index(request):
    try:
        current_user = request.user.id
        sc_token = SmartControlUser.objects.get(
            user=current_user).token
        sc_website = Website.objects.get(name='SmartControl').url
        sc_link = f"{sc_website}#!/?token={sc_token}"
        context = {
            'token': sc_token,
            'smartcontrol': sc_link,
        }
    except ObjectDoesNotExist:
        context = {
            'smartcontrol': 'http://smartcontrol.mitechnologiesinc.com',
        }

    return render(request, "index.html", context)


def login_view(request):
    form = LoginForm()
    if "sign-in" in request.POST:
        username = request.POST['username']
        password = request.POST['pswd']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Wrong username or password.')
            return redirect("login")
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect("login")


class EmployeeList(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class WebsiteList(ListCreateAPIView):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer


class WebsiteDetail(RetrieveUpdateDestroyAPIView):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer


class PartsDataUserList(ListCreateAPIView):
    queryset = PartsDataUser.objects.all()
    serializer_class = PartsDataUserSerializer


class PartsDataUserDetail(RetrieveUpdateDestroyAPIView):
    queryset = PartsDataUser.objects.all()
    serializer_class = PartsDataUserSerializer


class SmartControlUserList(ListCreateAPIView):
    queryset = SmartControlUser.objects.all()
    serializer_class = SmartControlUserSerializer


class SmartControlUserDetail(RetrieveUpdateDestroyAPIView):
    queryset = SmartControlUser.objects.all()
    serializer_class = SmartControlUserSerializer
