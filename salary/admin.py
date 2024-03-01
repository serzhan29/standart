from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'position', 'state', 'works_day', 'fact_dat', 'ratio', 'tariff_fund', 'raising',
                    'base_rate', 'week_1_4', 'week_5_9', 'week_10_11', 'home_learn_1', 'result', 'base_salary',
                    'skip_lesson', 'amount_1', 'replace_lesson', 'amount_2', 'position_salary_1', 'position_salary_2',
                    'total_result', 'ecology', 'allowance', 'hazard_1', 'hazard_2', 'total_amount_1', 'total_amount_2',
                    'classroom_teach', 'classroom_salary_1', 'classroom_salary_2', 'home_learn_2', 'home_learn_3',
                    'lesson_room_1', 'lesson_room_2', 'update', 'three_languages_1', 'three_languages_2', 'master_1',
                    'master_2', 'percent', 'category_1', 'category_2', 'head_teacher_1', 'head_teacher_2')
    list_filter = ('position', 'state', 'works_day', 'base_salary')
    search_fields = ('user_id', 'position')

admin.site.register(Employee, EmployeeAdmin)
