from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
import ProductDetail.views
from .views import UserApiView, UserDetailApi, send_mail

urlpatterns = [
    url(r'^$', UserApiView.as_view()),
    url(r'^(?P<pk>\d+)/$', UserDetailApi.as_view()),
    url('send', send_mail)
]
