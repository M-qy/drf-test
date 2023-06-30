# Generated by Django 3.1.5 on 2023-06-30 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='学校')),
                ('member', models.IntegerField(verbose_name='规模')),
                ('create_time', models.DateField(verbose_name='创建时间')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.SmallIntegerField(verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
