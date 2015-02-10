from django.contrib import admin

# Register your models here.

from .models import PrayerRequest

class PrayerRequestAdmin(admin.ModelAdmin):
	class Meta:
		models = PrayerRequest

admin.site.register(PrayerRequest, PrayerRequestAdmin)