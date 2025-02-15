from django.db import models

class Department(models.Model):
    department_id = models.CharField(max_length=100, verbose_name="شناسه دپارتمان", null=True, blank=True)
    department_name = models.CharField(max_length=255, unique=True, verbose_name="نام بخش", null=True, blank=True)
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")

    class Meta:
        verbose_name = 'واحد سازمان'
        verbose_name_plural = 'واحد های سازمان'

    def __str__(self):
        return self.department_name

class CorporatePersonnel(models.Model):
    personal_id = models.CharField(max_length=100, verbose_name="شناسه پرسنلی", null=True, blank=True)
    personnal_department_id = models.CharField(max_length=255, verbose_name="بخش",null=True, blank=True)
    personnal_first_name = models.CharField(max_length=100, verbose_name="نام", null=True, blank=True)
    personnal_last_name = models.CharField(max_length=100, verbose_name="نام خانوادگی", null=True, blank=True)
    personnal_phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="شماره تلفن")
    personnal_position = models.CharField(max_length=255, verbose_name="سمت شغلی", blank=True, null=True)
    personnal_date_hired = models.DateField(verbose_name="تاریخ استخدام", blank=True, null=True)
    personnal_type_status = models.CharField(max_length=20, default='active', verbose_name="نوع استخدام", null=True, blank=True)
    personnal_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="حقوق")
    personnal_address = models.TextField(blank=True, null=True, verbose_name="آدرس")
    personnal_melli_code = models.TextField(blank=True, null=True, verbose_name="کد ملی")
    personnal_birth_date = models.DateField(blank=True, null=True, verbose_name="تاریخ تولد")
    personnal_emergency_contact = models.CharField(max_length=255, blank=True, null=True, verbose_name="تماس اضطراری")

    class Meta:
        verbose_name = 'نیروی سازمان'
        verbose_name_plural = 'پرسنل سازمان'
        
    
    def __str__(self):
        return f"=> {self.personnal_first_name} {self.personnal_last_name} <="