# -*- coding:utf-8 -*-
__author__ = "cjluzzl"
__date__ = "2017/8/7 23:32 "

import xadmin
from .models import ArticleType, ArticleContent


class ArticleTypeAdmin(object):
    list_display = ['type_name', 'count']
    search_fields = ['type_name', 'count']
    list_filter = ['type_name', 'count']


class ArticleContentAdmin(object):
    list_display = ['type','title_name', 'pub_time',
                    'favorite_num', 'comment_num']
    search_fields = ['type__type_name','title_name',
                    'favorite_num', 'content']
    list_filter = ['type','title_name', 'pub_time',
                    'favorite_num', 'comment_num']
    style_fields = {"content": "ueditor"}




#xadmin.site.unregister(User)

xadmin.site.register(ArticleType, ArticleTypeAdmin)
xadmin.site.register(ArticleContent, ArticleContentAdmin)
