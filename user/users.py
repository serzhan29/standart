from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class AdditionUsers(AbstractUser):
    phone_number = PhoneNumberField('Номер телефон:', unique=True) 

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
