from django.db.models import Count, Sum
from django.http import HttpResponse
from django.shortcuts import redirect, render
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

from .forms import ExpenseForm
from .metrics import EXPENSE_CREATED_EVENTS, EXPENSE_RECORDS_TOTAL, EXPENSE_TOTAL_AMOUNT
from .models import Expense


def home(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            EXPENSE_CREATED_EVENTS .inc()
            return redirect('home')
    else:
        form = ExpenseForm()

    expenses = Expense.objects.all()[:10]
    summary = Expense.objects.aggregate(
        total_amount=Sum('amount'),
        expense_count=Count('id'),
    )

    context = {
        'form': form,
        'expenses': expenses,
        'total_amount': summary['total_amount'] or 0,
        'expense_count': summary['expense_count'] or 0,
    }

    return render(request, 'home.html', context)


def health(request):
    return HttpResponse("OK", content_type="text/plain")


def metrics(request):
    summary = Expense.objects.aggregate(
        expense_count=Count("id"),
        total_amount=Sum("amount"),
    )

    EXPENSE_RECORDS_TOTAL.set(summary["expense_count"] or 0)
    EXPENSE_TOTAL_AMOUNT.set(float(summary["total_amount"] or 0))

    return HttpResponse(generate_latest(), content_type=CONTENT_TYPE_LATEST)