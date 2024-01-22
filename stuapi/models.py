from django.db import models

# Create your models here.
class Student(models.Model):
    '''学生信息'''
    name = models.CharField(max_length=20,verbose_name='姓名')
    sex = models.CharField(max_length=10,verbose_name='性别')
    age = models.IntegerField(verbose_name='年龄')
    classmate = models.CharField(max_length=1000,verbose_name='班级编号')
    description = models.CharField(max_length=1000,verbose_name = '描述')
    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural=verbose_name