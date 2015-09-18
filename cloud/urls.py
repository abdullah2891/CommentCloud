from django.conf.urls import url
from . import views

__author__ = 'Abdullah_Rahman'

urlpatterns=[
    url(r'^$',views.view, name='post_image'),
    url(r'^test.png$',views.test,name='test'),
]