# Generated by Django 2.2.1 on 2019-09-23 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0011_auto_20190923_2115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='type',
            new_name='type_id',
        ),
    ]
