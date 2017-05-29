# coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.six import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Comment(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=255)
	url = models.URLField(blank=True)
	text = models.TextField()
	created_time = models.DateTimeField(auto_now_add=True)   # 当评论数据保存到数据库时，自动把created_time的值指定为当前时间

	post = models.ForeignKey('blog.Post')  # 一个评论只能属于一篇文章，一篇文章可以有多个评论

	def __str__(self):
		return self.text[:20]