from django.shortcuts import render
from django.views.generic.base import View
from .models import Blogs, Labels, Categorys
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
import re
from .forms import Contact
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.


class BlogListView(View):
    def get(self, request):
        lable = request.GET.get('lable', '')
        categorys = request.GET.get('categorys', '')
        # 标签
        lable_list = Labels.objects.all()

        # 类别
        categorys_list = Categorys.objects.all()

        # 最近的帖子
        lately_blogs = Blogs.objects.all()[:3]
        blogs_ranking_list = []
        for lately_blog in lately_blogs:
            blogs_ranking_dict = {}
            blogs_ranking_dict['title'] = lately_blog.title
            blogs_ranking_dict['id'] = lately_blog.id
            img = re.search('<img.*?src="(.*?)"[^>]*?>', lately_blog.content)
            try:
                blogs_ranking_dict['img'] = img.group(1)
            except:
                blogs_ranking_dict['img'] = None
            blogs_ranking_list.append(blogs_ranking_dict)

        # 博客内容
        if lable:
            blog_list = Blogs.objects.filter(lable=str(lable))
        elif categorys:
            blog_list = Blogs.objects.filter(blog_mondel=str(categorys))
        else:
            blog_list = Blogs.objects.all()
        # 重组博客内容
        rb_blog_list = []
        for blog in blog_list:
            rb_blog_dict = {}
            rb_blog_dict['add_time'] = blog.add_time
            rb_blog_dict['title'] = blog.title
            img = re.search('<img.*?src="(.*?)"[^>]*?>', blog.content)
            try:
                rb_blog_dict['img'] = img.group(1)
            except:
                rb_blog_dict['img'] = None
            rb_blog_dict['click_num'] = blog.click_num
            blog_content = blog.content
            dr = re.compile(r'<[^>]+>',re.S)
            start_content = dr.sub('',blog_content)
            rb_blog_dict['start_content'] = start_content[:90] + '...'
            rb_blog_list.append(rb_blog_dict)
            rb_blog_dict['id'] = blog.id

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(rb_blog_list, 6, request=request)
        all_blog =  p.page(page)

        return render(request, 'blog-list.html',{
            'lable_list': lable_list,
            'categorys_list': categorys_list,
            'blogs_ranking_list' : blogs_ranking_list,
            'all_blog' : all_blog,
        })


class BlogContentView(View):
    def get(self, request, blog_id):
        blog_content = Blogs.objects.get(id=int(blog_id))
        return render(request, 'blog-content.html', {
            'blog_content' : blog_content
        })


class ContactView(View):
    def post(self, request):

        blog_form = Contact(request.POST)
        if blog_form.is_valid():
            blog_form.save(commit=True)
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail"}', content_type='application/json')

