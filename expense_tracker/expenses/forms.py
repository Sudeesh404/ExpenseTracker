from django import forms
from .models import Expense
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ExpenseForm(forms.ModelForm):
    
    class Meta:
        model = Expense
        fields = ['amount', 'category','description'] #form fields
        widgets = {
            'description': forms.TextInput(attrs={'placeholder':'what was this expense for?'}),
        }
