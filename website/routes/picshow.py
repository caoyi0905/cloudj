from django.http import HttpResponseRedirect
from website.model.operate_file import pictureShow,getPicShareStauts


def my_view(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')

    if request.method=='GET':
        return pictureShow(request)

    if request.method=='POST':
        return getPicShareStauts(request)
