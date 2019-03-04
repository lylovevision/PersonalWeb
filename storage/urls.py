from django.conf.urls import url
from .views import IndexView, CollectionView, AboutView, page_not_found

app_name = 'homepage'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^collection$', CollectionView.as_view(), name='collection'),
    url(r'^about$', AboutView.as_view(), name='about')
]

handler404 = 'views.page_not_found'