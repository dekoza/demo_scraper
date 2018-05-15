from rest_framework import viewsets
from . import serializers
from . import models


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = models.Currency.objects.all()
    serializer_class = serializers.CurrencySerializer
    lookup_field = 'code'
    lookup_url_kwarg = 'code'


class RateViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RateSerializer
    filter_fields = ['date']

    def get_queryset(self):
        return models.Rate.objects.filter(currency__code=self.kwargs['currency_code'])
