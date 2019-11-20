from django.contrib import admin

from .models import IPAddress


class IPAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip_address']
    search_fields = ['ip_address']


admin.site.register(IPAddress, IPAddressAdmin)

