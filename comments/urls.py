# coding:utf-8
from django.conf.urls import url
from . import views

app_name = 'comments'   # 规定命名空间
urlpatterns = [
	url(r'^comment/post/(?P<post_pk>[0-9]+)/$',  views.post_comment, name='post_comment')
]