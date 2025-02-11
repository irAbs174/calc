from django.db import models

class User(models.Model):
    user_id = models.CharField(unique=True, max_length=16, verbose_name='شناسه کاربر', null=True, blank=True)
    user_name = models.CharField(max_length=65, verbose_name='نام کاربر', null=True, blank=True)
    email = models.CharField(max_length=65, verbose_name='ایمیل کاربر', blank=True)
    password = models.CharField(max_length=65, verbose_name='رمزعبور کاربر', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد کاربر')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آخرین بروز رسانی کاربر')
    objects = models.Manager()
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر ها'
        
    
    def __str__(self):
        return f"=> {self.user_name} <="