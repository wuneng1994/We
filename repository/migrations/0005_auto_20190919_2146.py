# Generated by Django 2.2.1 on 2019-09-19 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0004_auto_20190919_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporting',
            name='detail',
            field=models.TextField(verbose_name='故障详细描述'),
        ),
    ]