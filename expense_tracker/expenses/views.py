from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)  from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)  # Only show logged-in user's expenses
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  # Assign the logged-in user
            expense.save()
            return redirect('expense_list')  # Redirect to the expenses list
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})
