from django.contrib import admin
from .models import Department, CorporatePersonnel

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(CorporatePersonnel)
class CorporatePersonnelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'position', 'department', 'employment_status', 'date_hired')
    list_filter = ('employment_status', 'department', 'date_hired')
    search_fields = ('first_name', 'last_name', 'email', 'position')
    fieldsets = (
        ('اطلاعات شخصی', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'birth_date', 'address')}),
        ('اطلاعات شغلی', {'fields': ('position', 'department', 'date_hired', 'employment_status', 'salary')}),
        ('سایر اطلاعات', {'fields': ('profile_picture', 'emergency_contact')}),
    )
