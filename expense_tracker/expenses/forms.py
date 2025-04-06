from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    
    class Meta:
        model = Expense
        fields = ['amount', 'category','description'] #form fields
        widgets = {
            'description': forms.TextInput(attrs={'placeholder':'what was this expense for?'}),
        }
