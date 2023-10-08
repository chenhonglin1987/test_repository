from django.db import models


class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name='标题', max_length=32)


class Gradelist(models.Model):
    """部门表"""
    title = models.CharField(verbose_name='标题', max_length=32)


class Class(models.Model):
    cname = models.CharField(verbose_name='分类页面名', max_length=16)


class Userlist(models.Model):
    """员工表"""
    uname = models.CharField(verbose_name='账号', max_length=16)
    password = models.CharField(verbose_name='密码', max_length=64)
    name = models.CharField(verbose_name='姓名', max_length=16)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name='账户创建时间')
    # 无约束
    # depart_id = models.BigIntegerField(verbose_name='部门ID')

    # 有约束
    # - to,与哪张表关联
    # - to_field，与哪列关联
    # - on_delete=models.CASEADE 级联删除
    # - null=True, blank=True, on_delete=models.SET_NULL 可以为空
    depart = models.ForeignKey(to="Department", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)
    grade = models.ForeignKey(to="Gradelist", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)
    # - choices=gender_choices 在Django中对其进行约束
    gender_choices = (
        (1, "男"),
        (2, "女")
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)


# class Department_delete(models.Model):
#     del = models.Model.delete()