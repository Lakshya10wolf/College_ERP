# Generated by Django 3.0.5 on 2020-08-04 14:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200804_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_performance',
            name='Roll_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student_performance',
            name='subject',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher_attendance',
            name='Sign_in',
            field=models.TimeField(default=datetime.datetime(2020, 8, 4, 19, 47, 1, 946118)),
        ),
    ]
