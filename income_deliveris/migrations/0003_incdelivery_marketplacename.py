# Generated by Django 3.1.6 on 2021-02-07 09:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('income_deliveris', '0002_auto_20210207_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='incdelivery',
            name='marketplacename',
            field=models.CharField(default=datetime.datetime(2021, 2, 7, 9, 15, 11, 725332, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
