# Generated by Django 3.1.6 on 2021-02-06 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income_deliveris', '0010_auto_20210206_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incdelivery',
            name='accountFiverr',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='incdelivery',
            name='clientName',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='incdelivery',
            name='emailAddress',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='incdelivery',
            name='fiverrId',
            field=models.CharField(max_length=50),
        ),
    ]
