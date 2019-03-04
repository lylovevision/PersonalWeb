from django.conf.urls import url
from .views import BlogListView, BlogContentView, ContactView

app_name = 'blog'

urlpatterns = [
    url(r'list', BlogListView.as_view(), name='blog'),
    url(r'content/(?P<blog_id>\d+)/$', BlogContentView.as_view(), name='content'),
    url(r'contact', ContactView.as_view(), name='contact'),
]