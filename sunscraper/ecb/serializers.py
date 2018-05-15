from rest_framework import serializers
from rest_framework.reverse import reverse

from . import models


class CurrencySerializer(serializers.ModelSerializer):
    rates_url = serializers.SerializerMethodField()

    class Meta:
        model = models.Currency
        fields = '__all__'

    def get_rates_url(self, obj):
        return reverse('v1:currency_rates-list', kwargs={'currency_code': obj.code})


class RateSerializer(serializers.ModelSerializer):
    currency = serializers.CharField(source='currency.code')

    class Meta:
        model = models.Rate
        fields = '__all__'
