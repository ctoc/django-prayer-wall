from django.shortcuts import render_to_response
from models import PrayerRequest
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt                                          
@csrf_exempt 
def home(request):

    if request.method == 'GET':
        # fetch from data from db, give it to frontend
        return render_to_response('request.html', RequestContext(request))
    elif request.method == 'POST':
        context = request.POST
        prayerRequest = str(context['prayer_request'])
        name = ''
        email = ''
        if 'prayer_name' in context:
            name = str(context['prayer_name'])
        if 'prayer_email' in context:
            email = str(context['prayer_email'])
        req = PrayerRequest(name=name, email=email, request=prayerRequest, count=0)
        req.save()
        print "-----------------------"
        print PrayerRequest.objects.all()
        return render_to_response('request.html', RequestContext(request))
