# Generated by Django 3.0.5 on 2020-08-08 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20200804_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub',
            name='course',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sub',
            name='sem',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher_attendance',
            name='Sign_in',
            field=models.TimeField(default=datetime.datetime(2020, 8, 8, 14, 45, 26, 656830)),
        ),
    ]
