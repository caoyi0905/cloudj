from django.http import HttpResponseRedirect
from website.model.operate_file import deletePicture
from website.models import Picture
from django.contrib.auth.models import User

def my_view(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    username=request.user.username
    user=User.objects.filter(username=username)[0]
    picture=request.path.split('/')[-1]
    pictures=Picture.objects.filter(picture_name=picture,onner_id=user.id)
    if len(pictures)!=1:
        return HttpResponseRedirect('/mypic')
    pictures.delete()
    if not pictures[0].picture_name.find(username):
        return HttpResponseRedirect('/mypic')
    return deletePicture(picture)
