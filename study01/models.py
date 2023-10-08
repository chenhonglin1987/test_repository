from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32, default='Null')
    tel = models.CharField(max_length=11, default='Null')
    account = models.CharField(max_length=12, default='chenhonglin')
    password = models.CharField(max_length=16, null=True, blank=True)

# admin组件，控制输出字段，而非object
    def __str__(self):
        return self.name


class test(models.Model):
    name = models.CharField(max_length=32, default='uname')
    tel = models.CharField(max_length=11, default='Null')
    t_01 = models.CharField(max_length=12, default='Null')