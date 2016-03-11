#coding:utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from website.models import Picture
from django.contrib.auth.models import User
from Crypto.Cipher import AES
import random,os

def my_view(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        users=User.objects.filter(username=request.user.username)
        if len(users)!=1:
            return HttpResponseRedirect('/mypic')

        fileObj = request.FILES.get('your_file', None)
        if not fileObj:
            return HttpResponseRedirect('/mypic')
        fileContent=fileObj.read()
        file_name = '%s-%s' %(request.user.username, ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba',10)) )
        picture=Picture()
        picture.picture_name = file_name
        picture.IV = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba',16))
        picture.key = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba',16))
        picture.onner = users[0]
        file_full_path = os.path.join(settings.FILEPATH, file_name)
        obj = AES.new(picture.key,AES.MODE_CBC, picture.IV )
        picture.filled = 16 - len(fileContent)%16
        fileContent = fileContent+''.join(['0' for i in range(picture.filled)])
        fileContent = obj.encrypt(fileContent)
        dest = open(file_full_path,'wb+')
        dest.write(fileContent)
        dest.close()
        picture.save()
        return HttpResponseRedirect('/mypic')
    return HttpResponseRedirect('/')