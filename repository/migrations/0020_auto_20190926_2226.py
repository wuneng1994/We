# Generated by Django 2.2.1 on 2019-09-26 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0019_user_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account',
            field=models.CharField(max_length=128, unique=True, verbose_name='用户名'),
        ),
    ]
