# Generated by Django 3.0.5 on 2020-08-04 12:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200804_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_attendance',
            name='Sign_in',
            field=models.TimeField(default=datetime.datetime(2020, 8, 4, 17, 51, 29, 795791)),
        ),
    ]
