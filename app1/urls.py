from django.urls import path
from .views import create_expense, get_expense, filter_expenses_by_month, get_totals

urlpatterns = [
   path('expense-create/', create_expense, name = 'create_expense'),
   path('expenses/list/', get_expense, name = 'get_expense'),
   path('expense/month/<int:year>/<int:month>', filter_expenses_by_month),
   path('total/', get_totals)
]