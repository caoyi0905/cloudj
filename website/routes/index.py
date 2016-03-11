from django.shortcuts import render
from django.http import HttpResponseRedirect

def my_view(request):
    notLogin=False
    username=str(request.user)
    if not request.user.is_authenticated():
        notLogin=True
        username=None
    return render(request,'index.html',{'url':'index','notLogin':notLogin,'username':username})