# Generated by Django 3.0.5 on 2020-08-04 12:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_auto_20200802_1332'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cse_subjects',
            new_name='sub',
        ),
        migrations.RemoveField(
            model_name='teacher_attendance',
            name='Teacher_Id',
        ),
        migrations.AddField(
            model_name='teacher_attendance',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student_attendance',
            name='Roll_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student_performance',
            name='Roll_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teacher_attendance',
            name='Sign_in',
            field=models.TimeField(default=datetime.datetime(2020, 8, 4, 17, 51, 4, 928245)),
        ),
    ]