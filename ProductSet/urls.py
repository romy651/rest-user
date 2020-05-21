"""ProductInfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include, url
import ProductDetail.views
from django.conf import settings
from django.conf.urls.static import static
from musers.views import BenefApiView, BenefDetailApi
from .get_html import send_email, get_transaction, get_receipt_success, get_association

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/product/', ProductDetail.views.ProductList.as_view()),
    path('api/v1/product/add', ProductDetail.views.ProductCreate.as_view()),
    path('api/v1/product/<int:id>/',
         ProductDetail.views.ProductRetrieveUpdateDestroy.as_view()),
    path('api/v1/metric/', ProductDetail.views.MetricList.as_view()),
    path('api/v1/metric/add', ProductDetail.views.MetricCreate.as_view()),
    path('api/v1/metric/<int:id>/',
         ProductDetail.views.MetricRetrieveUpdateDestroy.as_view()),
    path('api/v1/issue/', ProductDetail.views.IssueList.as_view()),
    path('api/v1/issue/add', ProductDetail.views.IssueCreate.as_view()),
    path('api/v1/issue/<int:id>/',
         ProductDetail.views.IssueRetrieveUpdateDestroy.as_view()),
    url(r'^musers/', include('musers.urls')),
    url(r'^transactions/', include('transactions.urls')),
    url(r'^beneficiary/', BenefApiView.as_view()),
    url(r'^beneficiary/^(?P<pk>\d+)/$', BenefDetailApi.as_view()),
    url(r'^send_email/', send_email),
    url(r'^send_code/', get_transaction),
    url(r'^send_receipt/', get_receipt_success),
    url(r'^send_association/', get_association)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
