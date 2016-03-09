from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^category/(\d+)/$', views.category_view),
    url(r'article/(?P<pk>\d+)/?', views.article),
    #url(r'^', views.test, name='test'),
]