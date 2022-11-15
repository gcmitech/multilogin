"""multilogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from core.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('login/', login_view, name="login"),
    path('', index, name="index"),
    path('logout/', logout_view,  name="logout"),
    path('admin/', admin.site.urls),
    path('websites/<pk>', WebsiteDetail.as_view(), name='website_api'),
    path('websites/', WebsiteList.as_view(), name='website_list_api'),
    path('employees/<pk>', EmployeeDetail.as_view(), name='employee_api'),
    path('employees/', EmployeeList.as_view(), name='employee_list_api'),
    path('partsdatausers/<pk>', PartsDataUserDetail.as_view(), name='partsdatauser_api'),
    path('partsdatausers/', PartsDataUserList.as_view(), name='partsdatauser_list_api'),
    path('smartcontrolusers/<pk>', SmartControlUserDetail.as_view(), name='smartcontroluser_api'),
    path('smartcontrolusers/', SmartControlUserList.as_view(), name='smartcontroluser_list_api'),
]
