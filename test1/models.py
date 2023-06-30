from django.db import models


class User(models.Model):
    name = models.CharField(verbose_name='名字', max_length=32)
    age = models.SmallIntegerField(verbose_name='年龄')


class School(models.Model):
    name = models.CharField(primary_key=True, verbose_name='学校', max_length=32)
    member = models.IntegerField(verbose_name='规模')
    create_time = models.DateField(verbose_name='创建时间')
    id = models.IntegerField()
