from django.urls import path
from .views import EmployeeListView, EmployeeListAPIView

urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('api/employees/', EmployeeListAPIView.as_view(), name='employee-list'),
]
