

from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
import ProductDetail.views
from .views import TransactionApiView, TransactionDetailAPi

urlpatterns = [
    url(r'^$', TransactionApiView.as_view()),
    url(r'^(?P<pk>\d+)/$', TransactionDetailAPi.as_view()),
    #url(r'^(?P<id>.*)/$', TransactionDetailApi.as_view()),
    #url(r'^(?P<id>.*)/update/$', TransactionDeleteApi.as_view()),
    #url(r'^(?P<id>.*)/delete/$', TransactionDeleteApi.as_view())
]
