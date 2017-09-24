# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import UserProfile
from django.contrib.auth.hashers import make_password
from django.views.generic.base import View

# Create your views here.

class MobileLoginView(View):
    def post(self, request):
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(username=username, password=password)
        if user is not None:
            return HttpResponse("success")
        else:
            return HttpResponse("fail")


class MobileRegisterView(View):
    def post(self, request):
        user = UserProfile()
        user.username = request.POST.get("username","")
        user.password = make_password(request.POST.get("pwd",""))
        user.email = request.POST.get("email","")
        user.mobile = request.POST.get("phoneNumber","")
        user.gender = request.POST.get("gender","")
        try:
            user.save()
            return HttpResponse("success")
        except:
            return HttpResponse("fail")
