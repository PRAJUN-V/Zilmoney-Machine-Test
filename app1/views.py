from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ExpenseSerializer
from .models import Expense
from django.db.models import Sum

@api_view(['POST'])
def create_expense(request):
    serializer = ExpenseSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = 201)
    return Response(serializer.errors, status = 400)

@api_view(['GET'])
def get_expense(request):
    expenses = Expense.objects.all()
    serializer = ExpenseSerializer(expenses, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def filter_expenses_by_month(request, year, month):
    expenses = Expense.objects.filter(
        created_at__year = year, created_at__monthn=month
    )
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_totals(request):
    total_expense = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    total_salary = 5000
    remaining_amount = total_salary- total_expense

    return Response(
        {
            'total_expense' : total_expense,
            'total_salary' : total_salary,
            'remaining_amount': remaining_amount
        }
    )
