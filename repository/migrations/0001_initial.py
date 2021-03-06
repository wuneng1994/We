# Generated by Django 2.2.1 on 2019-09-19 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False, verbose_name='用户id')),
                ('username', models.CharField(max_length=25, verbose_name='用户名')),
                ('pwd', models.CharField(max_length=25, verbose_name='密码')),
                ('email', models.EmailField(max_length=255, verbose_name='邮箱')),
                ('img', models.ImageField(upload_to='static/user_img')),
            ],
            options={
                'verbose_name_plural': '用户信息',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False, verbose_name='博客id')),
                ('surfix', models.CharField(max_length=32, verbose_name='博客后缀')),
                ('theme', models.CharField(choices=[('blue', '蓝色'), ('red', '红色'), ('green', '绿色')], max_length=10, verbose_name='主题类型')),
                ('title', models.CharField(max_length=255, verbose_name='博客主题')),
                ('summary', models.TextField(blank=True, null=True, verbose_name='博客简介')),
                ('relationship', models.ManyToManyField(related_name='_blog_relationship_+', to='repository.Blog')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='repository.User')),
            ],
            options={
                'verbose_name_plural': '博客信息',
            },
        ),
    ]
