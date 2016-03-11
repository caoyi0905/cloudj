from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

def my_view(request):
    if request.method=='GET':
        return render(request,'signup.html')

    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']

    filterResult=User.objects.filter(username=username)
    if len(filterResult)>0:
        return HttpResponse('user is existed!')

    user = User.objects.create_user(username,email,password)
    newUser=authenticate(username=username,password=password)
    if newUser is not None:
        if newUser.is_active:
            login(request, newUser)
            return HttpResponse('success')
        else:
            return HttpResponse('disabled')
    else:
        return HttpResponse('invalid')
