from django.http import StreamingHttpResponse
from django.http import HttpResponse
from django.conf import settings
from website.models import Picture
from django.contrib.auth.models import User
from Crypto.Cipher import AES
import os

def big_file_download(request):
    def file_iterator(file_name, chunk_size=1024):
        with open(settings.FILEPATH+file_name,'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    the_file_name=request.path.split('/')[-1]
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(request.path.split('/')[-1])
    return response

def pictureShow(request):
    file_name =request.path.split('/')[-1]
    file_path=settings.FILEPATH+file_name
    if os.path.isdir(file_path):
        return HttpResponse('')

    username=request.user.username
    user=User.objects.filter(username=username)[0]

    res=Picture.objects.filter(onner_id=user.id,picture_name=file_name)
    if len(res)!=1:
        return HttpResponse('')

    obj = AES.new(res[0].key, AES.MODE_CBC,res[0].IV)
    f=open(file_path,'rb').read()
    fileContent=obj.decrypt(f)
    for i in range(res[0].filled):
        fileContent=fileContent[:-1]
    response = HttpResponse(fileContent)
    response['Content-Type']=''
    return response

def getPicShareStauts(request):
    file_name =request.path.split('/')[-1]
    file_path=settings.FILEPATH+file_name
    if os.path.isdir(file_path):
        return HttpResponse('')

    username=request.user.username
    user=User.objects.filter(username=username)[0]

    res=Picture.objects.filter(onner_id=user.id,picture_name=file_name)
    if len(res)!=1:
        return HttpResponse('')
    response='no'
    if res[0].isshared:
        response='yes'
    return HttpResponse(response)

def deletePicture(file_name):
    try:
        os.remove(settings.FILEPATH+file_name)
    except:
        return HttpResponse('err')
    response = HttpResponse('ok')
    return response