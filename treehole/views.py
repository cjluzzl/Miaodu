# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import json
from .models import TreeHoleArticle, TreeHoleArticleComment
from users.models import UserProfile
# Create your views here.

PERPAGER_ARTICLE_COUNT = 5


class TreeHolePubView(View):
    def post(self, request):
        article = TreeHoleArticle()
        content = request.POST.get("content","")
        user_tag = request.POST.get("user","")
        user = UserProfile.objects.get(username=user_tag)
        article.user = user
        article.content = content
        article.save()
        return HttpResponse("发布成功")

class TreeHoleFavAddView(View):
    def get(self, request, article_id):
        try:
            article = TreeHoleArticle.objects.get(pk=article_id)
            article.fav_count = article.fav_count + 1
            article.save()
            return HttpResponse(u"点赞成功",content_type="text/plain")
        except:
            print "出现异常"
            return HttpResponse(u"异常操作", content_type="text/plain")


class TreeHoleJsonListView(View):
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
        datas = TreeHoleArticle.objects.all()[::-1]

        datas = datas[(int(page_id) - 1) * PERPAGER_ARTICLE_COUNT:int(page_id) * PERPAGER_ARTICLE_COUNT]
        for data in datas:
            dic = {}
            dic["id"] = data.id
            dic["user"] = data.user.nick_name
            dic["userHeadUrl"] = "http://miaodu.cjluzzl.cn/" + "media/"+str(data.user.image)
            dic["content"] = data.content
            dic["pubTime"] = str(data.pub_time)
            dic["favCount"] = data.fav_count
            dic["commentNum"] = data.comment_count
            dic["address"] = data.address
            if data.comment_count == 0:
                dic["commentUrl"] = ""
            else:
                dic["commentUrl"] = "http://miaodu.cjluzzl.cn/treehole/comment/" + str(data.id) + "/1"
            l.append(dic)
        json_data["data"] = l
        if (int(page_id)) * PERPAGER_ARTICLE_COUNT < TreeHoleArticle.objects.count():
            json_data["more"] = "http://miaodu.cjluzzl.cn/treehole/get_json_data/" + str(int(page_id) + 1)
        else:
            json_data["more"] = ""

        return HttpResponse(json.dumps(json_data), content_type="application/json")


class TreeHoleCommentView(View):
    def get(self, request, article_id, page_id):
        json_data = {}
        try:
            int(article_id)
            int(page_id)
        except:
            json_data["retcode"] = "400"
            json_data["meta"] = "非法页面参数"
            return HttpResponse(json.dumps(json_data), content_type="application/json")

        comments = TreeHoleArticleComment.objects.filter(comment_article__pk = article_id)[::-1]

        comments = comments[(int(page_id) - 1) * PERPAGER_ARTICLE_COUNT:int(page_id) * PERPAGER_ARTICLE_COUNT]
        l = []
        for comment in comments:
            dic = {}
            dic["user"] = comment.user.nick_name
            dic["userHeadUrl"] = "http://miaodu.cjluzzl.cn/" +"media/"+ str(comment.user.image)
            dic["pubTime"] = str(comment.pub_time)
            dic["content"] = comment.comment_content
            l.append(dic)
        json_data["data"] = l
        if (int(page_id)) * PERPAGER_ARTICLE_COUNT < TreeHoleArticleComment.objects.filter(comment_article__pk = article_id).count():
            json_data["more"] = "http://miaodu.cjluzzl.cn/treehole/comment/" + article_id +"/"+ str(int(page_id) + 1)
        else:
            json_data["more"] = ""

        return HttpResponse(json.dumps(json_data), content_type="application/json")