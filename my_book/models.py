from django.db import models

# Create your models here.
# 创建模型

#定义图书模型类BookInfo
class BookInfo(models.Model):
    # 图书名称
    # btitle = models.CharField(max_length=20)
    btitle = models.CharField(max_length=20,db_column='title')
    # 日期
    bdate = models.DateField()
    # 阅读量
    bread = models.IntegerField(default=0)
    # 评论量
    bcommit = models.IntegerField(default=0)
    # 逻辑删除
    is_delete = models.BooleanField(default=False)
#定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    # 英雄姓名
    hname = models.CharField(max_length=20)
    # 英雄性别
    hgender = models.BooleanField(default=True)
    # 英雄描述
    hcommit = models.CharField(max_length=255,null=True,blank=False)
    # 逻辑删除
    is_delete = models.BooleanField(default=False)
    # 外键 英雄与图书表的关系为一对多，所以属性定义在英雄模型类中
    hbook = models.ForeignKey('BookInfo')