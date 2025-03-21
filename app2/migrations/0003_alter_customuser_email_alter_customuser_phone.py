# Generated by Django 5.1.6 on 2025-03-03 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_alter_customuser_email_alter_customuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='شماره تلفن'),
        ),
    ]
