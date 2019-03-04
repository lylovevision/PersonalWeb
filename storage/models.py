from django.db import models
from datetime import datetime

# Create your models here.


class Storage(models.Model):
    degree = models.CharField(verbose_name="分类", choices=(("wz", "网站"), ("rj", "软件"), ("qt", "其他")), max_length=4)
    add_time = models.DateTimeField(verbose_name="存储时间", default=datetime.now())
    url_path = models.CharField(verbose_name="存储地点", max_length=150)
    explain = models.TextField(verbose_name="简介")

    class Meta:
        verbose_name = "收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.degree


class CommonTools(models.Model):
    name = models.CharField(verbose_name="工具名称", max_length=15)
    url_path = models.CharField(verbose_name="工具来源", max_length=150)

    class Meta:
        verbose_name = "常用工具"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

