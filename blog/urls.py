# coding:utf-8
from django.conf.urls import url

from . import views

app_name = 'blog'   # 告诉Django这个是属于blog应用的urls.py模块
urlpatterns = [
	url(r'^$', views.index, name='index'),
	# (?P<pk>[0-9]+) 表示命名捕获组，其作用是从用户访问的 URL 里把括号
	# 内匹配的字符串捕获并作为关键字参数传给其对应的视图函数 detail。
	url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
	# 视图函数的调用就是这个样子：detail(request, pk=255)		 
	url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
	url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]