from django.urls import path

from .views import DjangoCountryData, geoip2_data


app_name = 'ip_address'


urlpatterns = [

    path('django-country-data/', DjangoCountryData.as_view(), name='django-country-data'),

    path('geoip2-data/', geoip2_data, name='geoip2-data'),

]




