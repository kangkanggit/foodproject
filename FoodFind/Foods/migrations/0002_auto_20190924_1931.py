# Generated by Django 2.1.8 on 2019-09-24 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foods', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='img',
            new_name='image',
        ),
        migrations.AddField(
            model_name='user',
            name='mail',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='邮件'),
        ),
    ]
