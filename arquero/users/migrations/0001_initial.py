# Generated by Django 3.0.5 on 2020-04-23 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clg_name', models.CharField(max_length=36)),
                ('clg_code', models.IntegerField()),
                ('uni_name', models.CharField(max_length=36)),
                ('user_name', models.CharField(max_length=36)),
            ],
        ),
    ]
