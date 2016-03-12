from django.conf.urls import url

from . import views

app_name = 'qa'
urlpatterns = [
    #url(r'^$', views.test, name='test'),
    url(r'^login/.*', views.test),
    url(r'^signup/.*', views.test),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.details, name='details'),
    url(r'^ask/', views.question_add,name='ask_question'),
    url(r'^popular/.*', views.post_list_popular),
    url(r'^answer/', views.answer_add),
    url(r'^new/.*', views.test),
    url(r'^', views.post_list_all),
]

