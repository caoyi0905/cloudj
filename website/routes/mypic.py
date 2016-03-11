from django.shortcuts import render
from website.model.getfile import getfiles
from django.http import HttpResponseRedirect
from django.conf import settings

def my_view(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    filelist=getfiles(settings.FILEPATH,request)
    username=request.user.username
    return render(request,'mypic.html',{'filelist':filelist,'url':'mypic','username':username})