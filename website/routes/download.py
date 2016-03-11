from django.http import HttpResponseRedirect
from website.model.operate_file import big_file_download

def my_view(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')

    return big_file_download(request)