from django.db import models
from django.utils.encoding import smart_unicode


# Create your models here.


class PrayerRequest(models.Model):
	name = models.CharField(max_length=120, default="Unknow")
	email = models.CharField(max_length=100, default="Empty")
	request = models.CharField(max_length=500, null=False, blank=False)
	count = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now_add=False, auto_now=True)
	
	def __unicode__(self):
		return smart_unicode(self.timestamp)
		