from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def my_view(request):
    logout(request)
    return HttpResponseRedirect('/')