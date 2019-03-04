from django.db import models
from datetime import datetime
# from DjangoUeditor.models import UEditorField
from DjangoUeditor.models import UEditorField
# Create your models here.


class Blogs(models.Model):
    title = models.CharField(max_length=30, verbose_name="标题")
    blog_mondel = models.ForeignKey('Categorys', verbose_name="博客类别", null=True, blank=True, default='', on_delete=models.SET_NULL)
    lable = models.ManyToManyField('Labels')
    content = UEditorField(verbose_name="文章内容", width=600, height=700, imagePath="blog/images/",
                          filePath="blog/files/", default='')
    add_time = models.DateTimeField(default=datetime.now(), verbose_name="添加时间")
    click_num = models.IntegerField(default=0, verbose_name="点赞量")
    class Meta:
        verbose_name = "博客"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Labels(models.Model):
    lable = models.CharField(max_length=7, verbose_name='标签名称')
    blog_lables = models.ManyToManyField('Blogs', verbose_name='博客')

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.lable


class Categorys(models.Model):
    mondel = models.CharField(max_length=20, verbose_name='博客类别', default='')

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.mondel


class Contact(models.Model):
    pen_name = models.CharField(max_length=15, verbose_name="笔名", default="无名")
    email = models.EmailField(verbose_name="邮箱")
    conten = models.TextField(max_length=500, verbose_name="内容")

    class Meta:
        verbose_name = "联系"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.pen_name


