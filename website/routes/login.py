from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login

def my_view(request):
    if request.method=='GET':
        return render(request,'login.html')

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse('success')
        else:
            return HttpResponse('disabled')
    else:
        return HttpResponse('invalid')
