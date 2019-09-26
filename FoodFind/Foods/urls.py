from django.contrib import admin
from django.urls import path,re_path
from Foods.views import *

urlpatterns = [
    re_path('login/',login),#登录页面,
    path('register/',register),#注册页面
    path('rajx/',ajx_register),#注册页面的ajx的验证
    path('index/',index),#主页的视图
    path('ajax_yz/',ajax_yz),#验证码的验证
    path('q_ajax/',q_ajax),#前端代码验证

]