# Generated by Django 3.0.5 on 2020-08-04 14:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0008_auto_20200804_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_attendance',
            name='Roll_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teacher_attendance',
            name='Sign_in',
            field=models.TimeField(default=datetime.datetime(2020, 8, 4, 19, 31, 28, 357561)),
        ),
    ]
