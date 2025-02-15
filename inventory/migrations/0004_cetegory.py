# Generated by Django 5.1.6 on 2025-02-11 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_inventory_inventory_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='cetegory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.CharField(blank=True, max_length=16, null=True, verbose_name='شناسه دسته بندی')),
                ('category_name', models.CharField(blank=True, max_length=16, null=True, verbose_name='نام دسته بندی')),
                ('category_desc', models.CharField(blank=True, max_length=16, null=True, verbose_name='توضیحات دسته بندی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد دسته بندی')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='آخرین بروز رسانی دسته بندی')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
    ]
