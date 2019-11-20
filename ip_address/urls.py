from django.urls import path

from .views import DjangoCountryData, geoip2_data, user_ip


app_name = 'ip_address'


urlpatterns = [

    # Django Country
    path('django-country-data/', DjangoCountryData.as_view(), name='django-country-data'),

    # Django GeoIP2
    path('geoip2-data/', geoip2_data, name='geoip2-data'),

    # Custom
    path('user-ip/', user_ip, name='user-ip'),

]




