from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(models.Model):
    name = models.CharField(verbose_name='名字', max_length=32)
    age = models.SmallIntegerField(verbose_name='年龄')


class School(models.Model):
    name = models.CharField(primary_key=True, verbose_name='学校', max_length=255)
    member = models.IntegerField(verbose_name='规模')
    create_time = models.DateField(verbose_name='创建时间')
    id = models.IntegerField()


class Author(models.Model):
    name = models.CharField(verbose_name='名字', max_length=32)
    time = models.DateField(verbose_name='出道时间')  # timezone.now().date()
    book_num = models.IntegerField(verbose_name='书籍数量')

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(verbose_name='书名', max_length=255)
    type = models.CharField(verbose_name='类型', max_length=32)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, related_name='books', to_field='id')
    price = models.DecimalField(verbose_name='价格', max_digits=10, decimal_places=2)
    press = models.CharField(verbose_name='出版社', max_length=255)


@receiver(post_save, sender=Book)
def create_book(sender, instance, created, **kwargs):
    if created:
        author_obj = instance.author
        author_obj.book_num += 1
        author_obj.save()
