# -*- coding:utf-8 -*-
__author__ = "cjluzzl"
__date__ = "2017/8/10 0:18 "

import xadmin
from .models import TinyReadArticle, TinyReadArticleComment


class TinyReadArticleAdmin(object):
    list_display = ["user", "content", "pub_time", "address"]
    search_fields = ["user", "content", "address"]
    list_filter = ["user", "content", "pub_time", "address"]


class TinyReadArticleCommentAdmin(object):
    list_display = ["user", "comment_article", "comment_content","pub_time"]
    search_fields = ["user", "comment_article", "comment_content"]
    list_filter = ["user", "comment_article", "comment_content","pub_time"]

xadmin.site.register(TinyReadArticle, TinyReadArticleAdmin)
xadmin.site.register(TinyReadArticleComment, TinyReadArticleCommentAdmin)