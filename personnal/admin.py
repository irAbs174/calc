from django.contrib import admin
from .models import Department, CorporatePersonnel

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'description')
    search_fields = ('department_name',)

@admin.register(CorporatePersonnel)
class CorporatePersonnelAdmin(admin.ModelAdmin):
    list_display = ('personnal_first_name', 'personnal_last_name', 'personnal_email', 'personnal_position', 'personnal_department', 'personnal_type_status', 'personnal_date_hired')
    list_filter = ('personnal_type_status', 'personnal_department', 'personnal_date_hired')
    search_fields = ('personnal_first_name', 'personnal_last_name', 'personnal_email', 'personnal_position')
    fieldsets = (
        ('اطلاعات شخصی', {'fields': ('personnal_first_name', 'personnal_last_name', 'personnal_email', 'personnal_phone_number', 'personnal_birth_date', 'personnal_address')}),
        ('اطلاعات شغلی', {'fields': ('personnal_position', 'personnal_department', 'personnal_date_hired', 'personnal_type_status', 'personnal_salary',)}),
        ('سایر اطلاعات', {'fields': ('personnal_emergency_contact',)}),
    )
