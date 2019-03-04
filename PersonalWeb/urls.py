"""PersonalWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
import xadmin
from django.views.static import serve
from .settings import MEDIA_ROOT
from django.views.generic.base import RedirectView


urlpatterns = [
    path(r'xadmin', xadmin.site.urls),
    # 使用富文本
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    # 使用blog
    path(r'blog', include('blogs.urls', namespace="blog")),
    # 使用blog
    path(r'', include('storage.urls', namespace="homepage")),
    # 显示图片
    url(r'^media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT},name='media'),
    # 配置富文本显示图片路径
    # url(r'^blog/(?P<path>.*)$', ),
    url(r'^favicon\.ioc$', RedirectView.as_view(url=r'static/img/icons/favicon.ico')),
]
