# Generated by Django 3.0.5 on 2020-08-08 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20200808_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_attendance',
            name='Sign_in',
            field=models.TimeField(default=datetime.datetime(2020, 8, 8, 19, 18, 46, 342148)),
        ),
    ]
