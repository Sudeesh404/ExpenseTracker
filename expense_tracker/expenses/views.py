from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import SignUpForm
from django.db.models import Sum
import json
from json import dumps as json_dumps
from django.contrib.auth import logout
from django.contrib.auth import logout
from django.conf import settings

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect('expense_list')
    else:
        form = SignUpForm()
    return render(request, 'expenses/signup.html', {'form': form})


@login_required
def expense_list(request):
    # Base queryset - only current user's expenses
    expenses = Expense.objects.filter(user=request.user)
    
    # Filter by category if selected
    category = request.GET.get('category')
    if category:
        expenses = expenses.filter(category=category)
    
    # Calculate totals
    total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    category_totals = expenses.values('category').annotate(total=Sum('amount'))

       # Prepare chart data
    category_labels = [cat['category'] for cat in category_totals]
    category_data = [float(cat['total']) for cat in category_totals]

    
    return render(request, 'expenses/expense_list.html', {
        'expenses': expenses,
        'total': total,
        'category_totals': category_totals,
        'categories': Expense.CATEGORIES,  # For dropdown filter
        'selected_category': category,    # To show current selection
        'category_labels': json.dumps(category_labels),
        'category_data': json.dumps(category_data),
    })

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

@login_required
def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk, user=request.user)  # Ensure user owns the expense
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/edit_expense.html', {'form': form})

@login_required
def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'expenses/delete_expense.html', {'expense': expense})


def custom_logout(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL or 'login')