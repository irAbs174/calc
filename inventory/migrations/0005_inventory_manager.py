# Generated by Django 5.1.6 on 2025-02-12 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_cetegory'),
    ]

    operations = [
        migrations.CreateModel(
            name='inventory_manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_id', models.CharField(blank=True, max_length=16, null=True, verbose_name='شناسه انباردار')),
                ('inventory_id', models.CharField(blank=True, max_length=16, null=True, verbose_name='شناسه انبار')),
                ('personnal_id', models.CharField(blank=True, max_length=16, null=True, verbose_name='شناسه پرسنلی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ تعریف انبار دار')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='آخرین بروز رسانی انباردار')),
            ],
            options={
                'verbose_name': 'انباردار',
                'verbose_name_plural': 'انباردار ها',
            },
        ),
    ]
