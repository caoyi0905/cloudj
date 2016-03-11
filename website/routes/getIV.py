from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.conf import settings
from website.models import Picture
from django.contrib.auth.models import User
import os

def my_view(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')

    if request.method=='GET':
        file_name =request.path.split('/')[-1]
        file_path=settings.FILEPATH+file_name
        if os.path.isdir(file_path):
            return HttpResponse('')

        username=request.user.username
        user=User.objects.filter(username=username)[0]

        res=Picture.objects.filter(onner_id=user.id,picture_name=file_name)
        if len(res)!=1:
            return HttpResponse('')
        res[0].isshared=True
        res[0].save()
        response = HttpResponse(res[0].IV)
        return response

    if request.method=='POST':
        file_name =request.path.split('/')[-1]
        file_path=settings.FILEPATH+file_name
        if os.path.isdir(file_path):
            return HttpResponse('')

        username=request.user.username
        user=User.objects.filter(username=username)[0]

        res=Picture.objects.filter(onner_id=user.id,picture_name=file_name)
        if len(res)!=1:
            return HttpResponse('')
        res[0].isshared=False
        res[0].save()
        response = HttpResponse('OK')
        return response