# Generated by Django 3.1.6 on 2021-02-11 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0011_remove_clientmanagement_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientmanagement',
            name='income',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='clientmanagement',
            name='outcome',
            field=models.FloatField(default=0.0),
        ),
    ]
