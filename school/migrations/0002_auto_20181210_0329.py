# Generated by Django 2.1.4 on 2018-12-10 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='username',
        ),
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
    ]
