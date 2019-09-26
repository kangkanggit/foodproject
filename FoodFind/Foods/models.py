from django.db import models

#用户的基本信息
class User(models.Model):
    username = models.CharField(max_length=32,verbose_name='用户名')
    password = models.CharField(max_length=32,verbose_name='密码')
    mail = models.EmailField(verbose_name='邮件',null=True,blank=True)
    image = models.ImageField(upload_to='static/img',verbose_name='用户头像',null=True,blank=True)


# Create your models here.
