# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from users.models import UserProfile
# Create your models here.


class TreeHoleArticle(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"发布人",default=1)
    content = models.CharField(max_length=200, verbose_name=u"树洞内容")
    pub_time = models.DateField(default=datetime.now, verbose_name=u"发布时间")
    fav_count = models.IntegerField(default=0, verbose_name=u"点赞数量")
    comment_count = models.IntegerField(default=0, verbose_name=u"评论数量")
    address = models.CharField(max_length=100, verbose_name=u"火星球")

    class Meta:
        verbose_name = u"树洞内容"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.content[0:len(self.content)/3]


class TreeHoleArticleComment(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"发布人")
    comment_article = models.ForeignKey(TreeHoleArticle, verbose_name=u"评论文章")
    pub_time = models.DateField(default=datetime.now, verbose_name=u"发布时间")
    comment_content = models.CharField(max_length=200,verbose_name=u"评论内容",default="评论")

    class Meta:
        verbose_name = u"评论信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return "评论人{0},被评论的人{1}".format(self.user, self.comment_article.user)

    def save(self, *args, **kwargs):
        #当提交评论时评论数 +1
        count = self.comment_article.comment_count
        self.comment_article.comment_count = count + 1
        print self.comment_article.comment_count
        self.comment_article.save()
        super(self.__class__, self).save(*args, **kwargs)