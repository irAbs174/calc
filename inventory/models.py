from django.db import models

class inventory(models.Model):
    inventory_id = models.CharField(unique=True, max_length=16, verbose_name='شناسه انبار', null=True, blank=True)
    inventory_name = models.CharField(max_length=65, verbose_name='نام انبار', null=True, blank=True)
    inventory_capacity = models.CharField(max_length=65, verbose_name='ظرفیت انبار', blank=True)
    inventory_location = models.CharField(max_length=65, verbose_name='موقعیت فیزیکی انبار', null=True, blank=True)
    personnal_id = models.CharField(max_length=65, verbose_name='متصدی انبار', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد انبار')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آخرین بروز رسانی انبار')
    objects = models.Manager()
    
    class Meta:
        verbose_name = 'انبار'
        verbose_name_plural = 'انبار ها'
        
    
    def __str__(self):
        return f"=> {self.inventory_name} <="