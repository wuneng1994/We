# Generated by Django 2.2.1 on 2019-09-19 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0005_auto_20190919_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporting',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='reporting',
            name='process_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='处理时间'),
        ),
    ]