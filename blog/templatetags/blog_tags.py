# coding:utf-8
# 自定义模板标签

from ..models import Post, Category
from django import template

register = template.Library()  # 实例化一个template.Library类

# 最新文章模板标签
@register.simple_tag          # 将函数get_recent_posts装饰为register.simple_tag
def get_recent_posts(num=5):
	return Post.objects.all().order_by('-created_time')[:num]

# 归档模板标签
@register.simple_tag
def archives():
	return Post.objects.dates('created_time', 'month', order='DESC')   # 按月份进行归档

# 分类模板标签
@register.simple_tag
def get_categories():
	return Category.objects.all()