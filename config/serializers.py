from rest_framework import serializers
from .models import (CryptoTable,)

class CryptoSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    price = serializers.IntegerField(required=True)
    one_hour_per = serializers.IntegerField(required=True)
    twenty_four_hour_per = serializers.IntegerField(required=True)
    seven_day_per = serializers.IntegerField(required=True)
    market_cap = serializers.IntegerField(required=True)
    volume = serializers.IntegerField(required=True)
    supply = serializers.IntegerField(required=True)

    class Meta:
        model = CryptoTable
        fields = '__all__'
