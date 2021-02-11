# Generated by Django 3.1.6 on 2021-02-11 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0007_auto_20210211_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='attendance',
        ),
        migrations.AddField(
            model_name='attendance',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Employees_emp_id', to='Employee.employees'),
        ),
    ]
