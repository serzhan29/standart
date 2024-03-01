from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Employee
from rest_framework import generics
from .serializers import EmployeeSerializer


class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем текущего пользователя
        user = self.request.user
        # Получаем объект пользователя из модели User
        user_info = User.objects.get(id=user.id)
        # Передаем имя пользователя и никнейм в контекст
        context['username'] = user_info.get_full_name()
        context['nickname'] = user_info.username
        return context

    def get_queryset(self):
        # Получаем queryset, содержащий только данные текущего пользователя
        queryset = super().get_queryset()
        # Получаем текущего пользователя
        user = self.request.user
        # Фильтруем queryset по полю user_id
        return queryset.filter(user_id=user.id)


class EmployeeListAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
