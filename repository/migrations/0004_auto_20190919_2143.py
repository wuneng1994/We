# Generated by Django 2.2.1 on 2019-09-19 13:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0003_userrelationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=255, verbose_name='博客标题'),
        ),
        migrations.AlterUniqueTogether(
            name='userrelationship',
            unique_together={('start', 'fans')},
        ),
        migrations.CreateModel(
            name='Reporting',
            fields=[
                ('UUID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='报障单号')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('detail', models.CharField(max_length=512, verbose_name='故障详细描述')),
                ('status', models.CharField(choices=[('unprocess', '待处理'), ('processing', '处理中'), ('processed', '已处理')], max_length=25, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('process_time', models.DateTimeField(blank=True, null=True)),
                ('processor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p', to='repository.User', verbose_name='处理者')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u', to='repository.User', verbose_name='提交用户')),
            ],
        ),
    ]
