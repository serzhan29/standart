from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    # employee_id = models.CharField(max_length=20, unique=True, verbose_name='ID сотрудника')
    # full_name = models.CharField(max_length=255, verbose_name='Фамилия Имя Отчество')
    position = models.CharField(max_length=255, verbose_name='Должность', blank=True, null=True)
    state = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Штат',  blank=True, null=True)
    works_day = models.IntegerField(verbose_name='Рабочие дни', blank=True, null=True)
    fact_dat = models.IntegerField(verbose_name='Факт рабочего дня', blank=True, null=True)
    ratio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Коэффициент', blank=True, null=True)
    tariff_fund = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Тарифная ставка', blank=True, null=True)
    raising = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Повышение 100 %', blank=True, null=True)
    base_rate = models.IntegerField(verbose_name='Основная ставка', blank=True, null=True)
    week_1_4 = models.IntegerField(verbose_name='Недельная нагрузка с 1 по 4', blank=True, null=True)
    week_5_9 = models.IntegerField(verbose_name='Недельная нагрузка с 5 по 9', blank=True, null=True)
    week_10_11 = models.IntegerField(verbose_name='Недельная нагрузка с 10 по 11', blank=True, null=True)
    home_learn_1 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Домашнее обучение - 1', blank=True, null=True)
    result = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Итог', blank=True, null=True)
    base_salary = models.IntegerField(verbose_name='Основная зарплата', blank=True, null=True)
    skip_lesson = models.IntegerField(verbose_name='Пропущенные уроки', blank=True, null=True)
    amount_1 = models.IntegerField(verbose_name='Сумма 1 ', blank=True, null=True)
    replace_lesson =  models.IntegerField(verbose_name='Замена урока', blank=True, null=True)
    amount_2 = models.IntegerField(verbose_name='Сумма 2', blank=True, null=True)
    position_salary_1 = models.IntegerField(verbose_name='Должностной оклад - 1', blank=True, null=True)
    position_salary_2 = models.IntegerField(verbose_name='Должностной оклад - 2', blank=True, null=True)
    total_result = models.IntegerField(verbose_name='Всего начисление', blank=True, null=True)
    ecology = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Экология 20 %', blank=True, null=True)
    allowance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Надбавка 10 % ', blank=True, null=True)
    hazard_1 = models.IntegerField(verbose_name='Вредность - 1', blank=True, null=True)
    hazard_2 = models.IntegerField(verbose_name='Вредность - 2', blank=True, null=True)
    total_amount_1 = models.IntegerField(verbose_name='Соммасы 1 - 11 д/т', blank=True, null=True)
    total_amount_2 = models.IntegerField(verbose_name='Соммасы 1 - 11 д/т', blank=True, null=True)
    classroom_teach = models.CharField(max_length=10, verbose_name='', blank=True, null=True)
    classroom_salary_1 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='зп кл.руководство - 1', blank=True, null=True)
    classroom_salary_2 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='зп кл.руководство - 2', blank=True, null=True)
    home_learn_2 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Домашнее обучение - 2',
                                       blank=True, null=True)
    home_learn_3 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Домашнее обучение - 3',
                                       blank=True, null=True)
    lesson_room_1 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='пән кабинет - 1', blank=True, null=True)
    lesson_room_2 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='пән кабинет - 2',
                                        blank=True, null=True)
    update = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Обнавленка',
                                 blank=True, null=True)
    three_languages_1 = models.IntegerField(verbose_name='три языка физ-ра - 1', blank=True, null=True)
    three_languages_2 = models.IntegerField(verbose_name='три языка физ-ра - 2', blank=True, null=True)
    master_1 = models.IntegerField(verbose_name='Магистр - 1', blank=True, null=True)
    master_2 = models.IntegerField(verbose_name='Магистр - 2', blank=True, null=True)
    percent = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='процент', blank=True, null=True)
    category_1 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Категория 1 процент', blank=True, null=True)
    category_2 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Категория 2 процент', blank=True, null=True)
    head_teacher_1 = models.IntegerField(verbose_name='Завуч надбавка - 1', blank=True, null=True)
    head_teacher_2 = models.IntegerField(verbose_name='Завуч надбавка - 2', blank=True, null=True)

    def __str__(self):
        return str(self.user_id)


