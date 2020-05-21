from rest_framework import serializers
from .models import Muser, Beneficiary
from django import forms


class MUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muser
        fields = (
            'id',
            'accountId',
            'name',
            'surname',
            'birthdate',
            'citezenship',
            'fname',
            'count',
            'mname',
            'email',
            'balance',
            'profile_photo',
            'passport_number',
            'password'
        )

    def validate_email(self, data):
        email = data
        return data


class BenefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiary
        fields = (
            'id',
            'owner',
            'name',
            'surname',
            'birthdate',
            'citezenship',
            'passport_number',
            'email'
        )

    def validate_email(self, data):
        email = data
        if Beneficiary.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "the given email is already registered")
        return data
