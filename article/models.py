# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField
# Create your models here.


class ArticleType(models.Model):
    type_name = models.CharField(max_length=20, verbose_name=u"文章类型")
    count = models.IntegerField(default=0,verbose_name=u"文章数量")

    class Meta:
        verbose_name = u"文章类型"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.type_name


class ArticleContent(models.Model):
    type = models.ForeignKey(ArticleType, verbose_name="所属文章类型")
    new_or_update = models.CharField(verbose_name=u"编辑类型",max_length=6,
                              choices=(('new', u"新建"), ('update', u"修改")), default="new")
    title_name = models.CharField(max_length=100, verbose_name=u"文章标题")
    title_image = models.ImageField(verbose_name=u"预览图片",upload_to="static/images/article_head/%Y/%m",
                                            default="static/images/article_head/default.png", max_length=100)
    pub_time = models.DateField(default=datetime.now,verbose_name=u"发布时间")
    favorite_num = models.IntegerField(default=0,verbose_name=u"点赞数量")
    comment_num = models.IntegerField(default=0,verbose_name=u"评论数量")
    content = UEditorField(width=900, height=600, imagePath="static/images/article/ueditor/",
                           filePath="static/file/article/ueditor/",verbose_name=u"文章内容")
    url = models.URLField(verbose_name="文章链接",default="http://miaodu.cjluzzl.cn/article/1/1.html")

    class Meta:
        verbose_name = u"文章详情"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title_name

    def save(self, *args, **kwargs):
        if self.new_or_update == "new":
            #修改文章url
            self.url = "http://miaodu.cjluzzl.cn/article/"+str(self.type.id)+"/"+str(ArticleContent.objects.count()+1)+".html"
            print "当前文章的url:",self.url
            #对应文章类型下文章数量增加1
            self.type.count = self.type.count + 1
            print "当前的数量 ",self.type.count
            self.type.save()
        else:
            #修改的时候传给什么值就赋值什么
            pass
        super(self.__class__, self).save(*args, **kwargs)

