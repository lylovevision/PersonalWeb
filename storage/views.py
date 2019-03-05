from django.shortcuts import render, render_to_response
from django.views.generic.base import View
from .models import CommonTools, Storage
from blogs.models import Blogs
import re
# Create your views here.


class IndexView(View):
    def get(self, request):
        tool_all = CommonTools.objects.all()

        # 博客内容
        blog_list = Blogs.objects.all().order_by("-add_time")[:3]
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
            dr = re.compile(r'<[^>]+>', re.S)
            start_content = dr.sub('', blog_content)
            rb_blog_dict['start_content'] = start_content[:90] + '...'
            rb_blog_list.append(rb_blog_dict)
            rb_blog_dict['id'] = blog.id
        return render(request, 'index.html', {
            'tool_all' : tool_all,
            'blog_all' : rb_blog_list
        })


class CollectionView(View):
    def get(self, requst):
        storage_all = Storage.objects.all()
        return render(requst, 'collection.html', {
            'storage_all' : storage_all
        })


class AboutView(View):
    def get(self,request):
        return render(request, 'about.html')


def page_not_found(request):
    return render_to_response('404.html')