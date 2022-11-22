from django.contrib.admin import ModelAdmin, site
from django.contrib.auth.admin import UserAdmin

from .models import *

site.site_header = 'Multilogin'
site.index_title = 'Multilogin Administration'
site.site_title = 'Multilogin Admin'


class SmartControlAdmin:
    using = 'SmartControl'


class EmployeeAdmin(UserAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name',
                    'email', 'is_staff', 'is_active', 'last_login', 'date_joined')


class PartsDataUserAdmin(ModelAdmin):
    list_display = ('id', 'user', 'name')


class SmartControlUserAdmin(ModelAdmin):
    list_display = ('id', 'user', 'name', 'last_login', 'due_date')


class BinManagerUserAdmin(ModelAdmin):
    list_display = ('id', 'name', 'surname', 'email')


class WebsiteAdmin(ModelAdmin):
    list_display = ('id', 'name', 'url')


site.register(Employee, EmployeeAdmin)
site.register(PartsDataUser, PartsDataUserAdmin)
site.register(SmartControlUser, SmartControlUserAdmin)
site.register(BinManagerUser, BinManagerUserAdmin)
site.register(Website, WebsiteAdmin)
