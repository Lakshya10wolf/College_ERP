# Generated by Django 3.0.5 on 2020-08-11 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20200811_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_attendance',
            name='Sign_in',
            field=models.TimeField(default=datetime.datetime(2020, 8, 11, 23, 16, 7, 787618)),
        ),
    ]
