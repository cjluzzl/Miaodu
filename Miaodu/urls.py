"""Miaodu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve
import xadmin


from Miaodu.settings import MEDIA_ROOT, STATIC_ROOT, STATIC_URL
from django.conf.urls.static import static

from article.views import ArticleListView, ArticleDetailView, ArticleJsonListView
from tinyread.views import TinyReadJsonListView, TinyReadFavAddView, TinyReadCommentView, PubTinyReadView, TinyReadPostComment
from treehole.views import TreeHoleJsonListView, TreeHoleCommentView, TreeHoleFavAddView, TreeHolePubView
from users.views import MobileLoginView, MobileRegisterView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),
    url(r"^get_article_list/",ArticleListView.as_view(),name="get_article_list"),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^article/(?P<typeid>.*)/(?P<articleid>.*)\.html', ArticleDetailView.as_view(),name="article_detail"),
    url(r'^article/get_json_data/(?P<page_id>.*)', ArticleJsonListView.as_view(), name="get_article_json_data"),
    url(r'^article/pub/', PubTinyReadView.as_view(), name="pub_tiny_read"),

    url(r'^tinyread/get_json_data/(?P<page_id>.*)', TinyReadJsonListView.as_view(),name="get_tiny_read_json_data"),
    url(r'^tinyread/fav_add/(?P<article_id>.*)', TinyReadFavAddView.as_view(), name="tiny_read_fav_add"),
    url(r'^tinyread/comment/(?P<article_id>.*)/(?P<page_id>.*)',TinyReadCommentView.as_view(), name="tiny_read_comment_json"),
    url(r'tinyread/post_comment/(?P<article_id>.*)',TinyReadPostComment.as_view(), name="tiny_read_post_comment"),


    url(r'^treehole/get_json_data/(?P<page_id>.*)', TreeHoleJsonListView.as_view(), name="get_tree_hole_json_data"),
    url(r'^treehole/fav_add/(?P<article_id>.*)', TreeHoleFavAddView.as_view(), name="tree_hole_fav_add"),
    url(r'^treehole/comment/(?P<article_id>.*)/(?P<page_id>.*)', TreeHoleCommentView.as_view(),
        name="tree_hole_comment_json"),
    url(r'treehole/pub/',TreeHolePubView.as_view(), name="tree_hole_pub"),

    url(r'^users/mobile_login/$', MobileLoginView.as_view(), name="mobile_login"),
    url(r'^users/mobile_register/$', MobileRegisterView.as_view(), name="mobile_register"),

]
