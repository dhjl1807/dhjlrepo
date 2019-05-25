from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, verbose_name='用户名', unique=True, null=False)
    password = models.CharField(max_length=20, verbose_name='用户密码', null=False)
    telephone = models.CharField(max_length=15, verbose_name='手机号码', unique=True, null=False)

    class Meta:
        db_table = 'User'
