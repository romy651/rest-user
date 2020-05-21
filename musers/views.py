from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Muser, Beneficiary
from .serializsers import MUserSerializer, BenefSerializer
from rest_framework import generics, mixins
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail as sm

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from email.message import EmailMessage
import smtplib


class UserApiView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Muser.objects.all()
    serializer_class = MUserSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        qs = Muser.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(email__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        file_serializer = MUserSerializer(data=request.data)

        return self.create(request, *args, **kwargs)


class UserDetailApi(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    queryset = Muser.objects.all()
    serializer_class = MUserSerializer
    parser_classes = (MultiPartParser, FormParser)

    def put(self, request, *args, **kwargs):
        file_serializer = MUserSerializer(data=request.data)
        if(file_serializer.is_valid()):
            file_serializer.save()
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class BenefApiView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Beneficiary.objects.all()
    serializer_class = BenefSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        qs = Beneficiary.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(email__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        file_serializer = BenefSerializer(data=request.data)

        return self.create(request, *args, **kwargs)


class BenefDetailApi(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    queryset = Beneficiary.objects.all()
    serializer_class = BenefSerializer
    parser_classes = (MultiPartParser, FormParser)

    def put(self, request, *args, **kwargs):
        file_serializer = BenefSerializer(data=request.data)
        if(file_serializer.is_valid()):
            file_serializer.save()
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


"""
def send_mail(request):
    res = sm(
        subject='Subject here',
        message='Here is the message.',
        from_email='keukouachancelin@gmail.com',
        recipient_list=['berio7993@gmail.com'],
        fail_silently=False,
    )

    return HttpResponse(f"Email sent to {res} members")
"""


def send_mail(request):

    msg = EmailMessage()
    msg['Subject'] = "info about your account"
    msg['From'] = 'keukouachancelin@gmail.com'
    msg['To'] = 'berio7993@gmail.com'
    msg.set_content('how avout goit ther today ')
    msg.add_alternative(content, subtype='html')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('keukouachancelin@gmail.com', '123consulting')
        smtp.send_message(msg)
    return HttpResponse(f"the message is sent")
