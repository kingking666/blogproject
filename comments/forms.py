# coding:utf-8
# 用来存放表单代码
from django import forms
from .models import Comment

# 如果表单对应有一个数据库模型（例如这里的评论表单对应着评论模型），那么使用 ModelForm 类会简单很多
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment   #表明这个表单对应的数据库模型是Comment类
		fields = ['name', 'email', 'url', 'text']  # 表单需要显示的字段