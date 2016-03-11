#coding:utf-8

from django.shortcuts import render
from django.http import HttpResponseRedirect
from website.models import Picture
from django.contrib.auth.models import User
import random

def my_view(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    username=request.user.username
    if request.method=='GET':
        return render(request,'share.html',{'url':'share','username':username})

    IV=request.POST['key']
    if len(IV)!=16:
        return render(request,'share.html',{'url':'share','username':username,'msg':'提取码不正确！'})

    pictures=Picture.objects.filter(IV=IV)

    if len(pictures)<1:
        return render(request,'share.html',{'url':'share','username':username,'msg':'提取码不正确！'})

    if pictures[0].isshared==False:
        return render(request,'share.html',{'url':'share','username':username,'msg':'该图片没有被分享！'})
    picture=pictures[0]

    user=User.objects.filter(username=username)[0]

    if picture.onner==user:
        return render(request,'share.html',{'url':'share','username':username,'msg':'你有这张图片了！'})

    newpicture=Picture()
    newpicture.picture_name = picture.picture_name
    newpicture.IV = picture.IV
    newpicture.key = picture.key
    newpicture.filled = picture.filled
    newpicture.onner = user
    newpicture.save()
    return render(request,'share.html',{'url':'share','username':username,'msg':'图片已加入个人图库！'})
