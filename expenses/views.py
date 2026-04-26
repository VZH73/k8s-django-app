from django.db.models import Count, Sum
from django.shortcuts import redirect, render

from .forms import ExpenseForm
from .models import Expense


def home(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExpenseForm()

    expenses = Expense.objects.all()[:10]
    summary = Expense.objects.aggregate(total_amount=Sum('amount'), expense_count=Count('id'))

    context = {
        'form': form,
        'expenses': expenses,
        'total_amount': summary['total_amount'] or 0,
        'expense_count': summary['expense_count'] or 0,
    }
    return render(request, 'home.html', context)
