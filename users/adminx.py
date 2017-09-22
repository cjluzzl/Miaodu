# -*- coding:utf-8 -*-
__author__ = "cjluzzl"
__date__ = "2017/8/7 23:05 "

import xadmin
from xadmin import views
from .models import EmailRevifyRecord
from .models import Banner, UserProfile
from xadmin.plugins.auth import UserAdmin
from django.contrib.auth.models import User
from xadmin.layout import Fieldset, Main, Side, Row, FormHelper




#主题注册
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


#更改网站标题和公司名注册
class GlobalSetting(object):
    site_title = u"秒读App资源后台管理系统"
    site_footer = u"power by cjluzzl"
    menu_style = "accordion"


class EmailRevifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time', 'is_alive']
    search_fields = ['code', 'email', 'send_type', 'is_alive']
    list_filter = ['code', 'email', 'send_type', 'send_time', 'is_alive']


class BannerAdmin(object):
    list_display = ['title','image', 'url', 'index', 'add_time']
    search_fields = ['title','image', 'url', 'index']
    list_filter = ['title','image', 'url', 'index', 'add_time']






#xadmin.site.unregister(User)

xadmin.site.register(EmailRevifyRecord, EmailRevifyRecordAdmin)
xadmin.site.register(Banner , BannerAdmin)
#xadmin.site.register(UserProfile , UserProfileAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)#主题注册
xadmin.site.register(views.CommAdminView, GlobalSetting)#更改网站标题和公司名注册