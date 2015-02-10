from django.contrib import admin

# Register your models here.

from .models import PrayerRequest

class PrayerRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'request', 'count', 'timestamp')
    class Meta:
        models = PrayerRequest

admin.site.register(PrayerRequest, PrayerRequestAdmin)