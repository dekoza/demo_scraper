from rest_framework import serializers
from . import models


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Currency
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rate
        fields = '__all__'
