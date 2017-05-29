# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
import markdown
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from comments.forms import CommentForm
from .models import Post, Category

def index(request):
	#render函数会根据我们传入的参数来构造HttpResponse
	post_list = Post.objects.all().order_by('-created_time')  # "-"表示逆序
	return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.body = markdown.markdown(post.body,
								  extensions=[        # extensions是对Markdown语法的拓展
								  	'markdown.extensions.extra',    # extra本身包含很多拓展
								  	'markdown.extensions.codehilite',   #　语法高亮拓展
								  	'markdown.extensions.toc',         # toc允许我们自动生成目录
								  	])
	form = CommentForm()
	# 获取这篇post下的全部评论
	comment_list = post.comment_set.all()
	#将文章、表单、以及文章下的评论列表作为模板变量传给detail.html模板，以便渲染相应数据
	context = {'post': post,
			   'form': form,
			   'comment_list': comment_list
			   }
	return render(request, 'blog/detail.html', context=context)

def archives(request, year, month):
	post_list = Post.objects.filter(created_time__year = year,    # 因为是函数的参数列表，所以Django要求把点换成两个下划线
									created_time__month = month,
									).order_by('-created_time')
	return render(request, 'blog/index.html', context={'post_list': post_list})

def category(request, pk):
	cate = get_object_or_404(Category, pk=pk)
	post_list = Post.objects.filter(category=cate).order_by('-created_time')
	return render(request, 'blog/index.html', context={'post_list': post_list})