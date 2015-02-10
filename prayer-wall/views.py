from django.shortcuts import render_to_response
from models import PrayerRequest
from django.template import RequestContext

def home(request):

    if request.method == 'GET':
        # fetch from data from db, give it to frontend
        return render_to_response('index.html', RequestContext(request))
    elif request.method == 'POST':
        prayerRequest = str(request.POST['prayer-request'])
        name = ''
        email = ''
        if 'prayer-name' in request.POST:
            name = str(request.POST['prayer-name'])
        if 'prayer-email' in request.POST:
            email = str(request.POST['prayer-email'])
        req = PrayerRequest(name=name, email=email, request=prayerRequest, count=0)
        req.save()
        print "-----------------------"
        print PrayerRequest.objects.all()
        return render_to_response('index.html', RequestContext(request))
