from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.gis.geoip2 import GeoIP2


# Django Country Data
class DjangoCountryData(TemplateView):
    template_name = 'ip_address/django_country_data.html'


# GeoIP2 Data
def geoip2_data(request):
    g_country = GeoIP2('/home/siyam/Desktop/visitor_ip_address/ip_address/geoip/GeoLite2-Country.mmdb')
    g_city = GeoIP2('/home/siyam/Desktop/visitor_ip_address/ip_address/geoip/GeoLite2-City.mmdb')

    country_data = g_country.country('google.com')
    city_data = g_city.city('72.14.207.99')

    context = {
        'country_data': country_data,
        'city_data': city_data,
    }

    template = 'ip_address/geoip2_data.html'

    return render(request, template, context)
