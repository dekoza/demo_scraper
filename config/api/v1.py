from django.conf.urls import url
from django.urls import include
from rest_framework_nested import routers

from sunscraper.ecb import views as ecb_views

# v1_router = routers.DefaultRouter()
v1_router = routers.SimpleRouter()

v1_router.register(r'currencies', ecb_views.CurrencyViewSet)

currency_router = routers.NestedSimpleRouter(v1_router, r'currencies', lookup='currency')
currency_router.register(r'rates', ecb_views.RateViewSet, base_name='currency_rates')


urlpatterns = [
    url(r'^', include(v1_router.urls)),
    url(r'^', include(currency_router.urls)),
]
