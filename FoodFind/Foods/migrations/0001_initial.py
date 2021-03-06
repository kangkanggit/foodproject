# Generated by Django 2.1.8 on 2019-09-23 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('img', models.ImageField(blank=True, null=True, upload_to='static/img', verbose_name='用户头像')),
            ],
        ),
    ]
