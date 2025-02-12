from django.contrib import admin
from .models import Department, CorporatePersonnel

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'description')
    search_fields = ('department_name',)

@admin.register(CorporatePersonnel)
class CorporatePersonnelAdmin(admin.ModelAdmin):
    list_display = ('personnal_first_name', 'personnal_last_name', 'personnal_position', 'personnal_department_id', 'personnal_type_status', 'personnal_date_hired')
    list_filter = ('personnal_type_status', 'personnal_department_id', 'personnal_date_hired')
    search_fields = ('personnal_first_name', 'personnal_last_name', 'personnal_position')