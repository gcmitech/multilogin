from django.forms import ModelForm
from .models import Employee

class LoginForm(ModelForm):
    class Meta:
        model = Employee        
        fields = ['username', 'password']
