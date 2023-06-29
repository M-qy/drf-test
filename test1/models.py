from django.db import models


class User(models.Model):
    name = models.CharField(verbose_name='名字', max_length=32)
    age = models.IntegerField(verbose_name='年龄')
