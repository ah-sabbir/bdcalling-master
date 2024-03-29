# Generated by Django 3.1.6 on 2021-02-07 08:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('income_deliveris', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incdelivery',
            name='client_fiverr_profile',
            field=models.CharField(default=datetime.datetime(2021, 2, 7, 8, 29, 6, 268309, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='incdelivery',
            name='client_email_address',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='incdelivery',
            name='order_amount_minus_percentage',
            field=models.FloatField(blank=True, default=20.0, null=True),
        ),
    ]
