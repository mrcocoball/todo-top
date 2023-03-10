# Generated by Django 4.1.7 on 2023-03-10 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='todo_complete_count',
            field=models.BigIntegerField(null=True, verbose_name='TODO_COMPLETE_COUNT'),
        ),
        migrations.AddField(
            model_name='user',
            name='todo_count',
            field=models.BigIntegerField(null=True, verbose_name='TODO_COUNT'),
        ),
    ]
