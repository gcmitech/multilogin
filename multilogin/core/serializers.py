from rest_framework.serializers import ModelSerializer
from .models import *


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class WebsiteSerializer(ModelSerializer):
    class Meta:
        model = Website
        fields = '__all__'


class PartsDataUserSerializer(ModelSerializer):
    class Meta:
        model = PartsDataUser
        fields = '__all__'


class SmartControlUserSerializer(ModelSerializer):
    class Meta:
        model = SmartControlUser
        fields = '__all__'
