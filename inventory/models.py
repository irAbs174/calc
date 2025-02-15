from django.db import models

class inventory(models.Model):
    inventory_id = models.CharField(max_length=16, verbose_name='شناسه انبار', null=True, blank=True)
    inventory_name = models.CharField(max_length=65, verbose_name='نام انبار', null=True, blank=True)
    inventory_capacity = models.CharField(max_length=65, verbose_name='ظرفیت انبار', blank=True)
    inventory_location = models.CharField(max_length=65, verbose_name='موقعیت فیزیکی انبار', null=True, blank=True)
    personnal_id = models.CharField(max_length=65, verbose_name='متصدی انبار', null=True, blank=True)
    inventory_category = models.CharField(max_length=65, verbose_name='دسته بندی انبار', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد انبار')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آخرین بروز رسانی انبار')
    objects = models.Manager()
    
    class Meta:
        verbose_name = 'انبار'
        verbose_name_plural = 'انبار ها'
        
    
    def __str__(self):
        return f"=> {self.inventory_name} <="

class cetegory(models.Model):
    category_id = models.CharField(max_length=16, verbose_name='شناسه دسته بندی', null=True, blank=True)
    category_name = models.CharField(max_length=16, verbose_name='نام دسته بندی', null=True, blank=True)
    category_desc = models.CharField(max_length=16, verbose_name='توضیحات دسته بندی', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد دسته بندی')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آخرین بروز رسانی دسته بندی')
    objects = models.Manager()
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        
    
    def __str__(self):
        return f"=> {self.category_name} <="

class inventory_manager(models.Model):
    manager_id = models.CharField(max_length=16, verbose_name='شناسه انباردار', null=True, blank=True)
    personnal_id = models.CharField(max_length=16, verbose_name='شناسه پرسنلی', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ تعریف انبار دار')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آخرین بروز رسانی انباردار')
    objects = models.Manager()
    
    class Meta:
        verbose_name = 'انباردار'
        verbose_name_plural = 'انباردار ها'
        
    
    def __str__(self):
        return f"=> {self.manager_id} <="