# Generated by Django 3.1.6 on 2021-02-11 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0008_auto_20210211_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='employee',
            new_name='emp_id',
        ),
    ]
