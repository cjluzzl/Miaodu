# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from article.models import ArticleContent
from django.http import HttpResponse
import json

#每页加载文章的数量
PERPAGER_ARTICLE_COUNT = 5


class ArticleListView(View):
    def get(self,request):
        all_article = ArticleContent.objects.all()
        return render(request,"article_list.html",{"all_article":all_article})


class ArticleDetailView(View):
    def get(self, request, typeid, articleid):
        article = ArticleContent.objects.get(pk=articleid)
        return render(request, "article_detail.html",{"article":article})


class ArticleJsonListView(View):
    def get(self, request, page_id):

        json_data = {}
        try:
            int(page_id)

        except:
            json_data["retcode"] = "400"
            json_data["meta"] = "非法页面参数"
            return HttpResponse(json.dumps(json_data), content_type="application/json")
        json_data["retcode"] = "200"
        json_data["meta"] = "请求成功"
        l = []
        articles = ArticleContent.objects.all()[::-1]
        articles = articles[(int(page_id)-1)*PERPAGER_ARTICLE_COUNT:int(page_id)*PERPAGER_ARTICLE_COUNT]

        for article in articles:
            dic = {}
            dic["title"] = article.title_name
            dic["image"] = "miaodu.cjluzzl.cn/media/"+str(article.title_image)
            dic["type"] = article.type.type_name
            dic["url"] = article.url
            l.append(dic)
        json_data["data"] = l
        if (int(page_id))*PERPAGER_ARTICLE_COUNT < ArticleContent.objects.count():
            json_data["more"] = "miaodu.cjluzzl.cn/article/get_json_data/" + str(int(page_id)+1)
        else:
            json_data["more"] = ""

        return HttpResponse(json.dumps(json_data),content_type="application/json")




