#coding:utf-8
from website.models import Picture
from django.contrib.auth.models import User

def getfiles(filepath,request):
    username=request.user.username
    user=User.objects.filter(username=username)[0]
    pictures=Picture.objects.filter(onner_id=user.id)
    lis=[]
    for pic in pictures:
        lis.append(pic.picture_name)
    return lis


