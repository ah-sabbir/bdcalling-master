# Generated by Django 3.1.6 on 2021-02-11 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0005_auto_20210211_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='clientManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='employees',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='head_of_department',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='head_of_department',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='last_name',
        ),
        migrations.AddField(
            model_name='attendance',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='attendance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clientManagement_attendance', to='Employee.attendance'),
        ),
        migrations.AddField(
            model_name='employees',
            name='emp_id',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employees',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='employees',
            name='phone',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employees',
            name='revenue',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attendance',
            field=models.CharField(choices=[('absent', 'Absent'), ('present', 'Present')], max_length=8),
        ),
        migrations.AlterField(
            model_name='employees',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.DeleteModel(
            name='Head_of_department',
        ),
        migrations.AddField(
            model_name='clientmanagement',
            name='attendance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Employees_attendance', to='Employee.employees'),
        ),
        migrations.AddField(
            model_name='clientmanagement',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Employees_name', to='Employee.employees'),
        ),
    ]
