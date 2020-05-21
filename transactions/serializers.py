from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'user',
            'description',
            'deposit',
            'withdrawal',
            'date'
        ]

    def validate(self, attrs):
        if (not attrs.get('deposit') == 0)and (not attrs.get('withdrawal')) == 0:
            raise serializers.ValidationError(
                'both deposit and withdrwal cannot be not null at the same time')
        if attrs.get('deposit') == 0 and attrs.get('withdrawal') == 0:
            raise serializers.ValidationError(
                'both deposit and withdrwal cannot be null at the same time')
        return attrs
