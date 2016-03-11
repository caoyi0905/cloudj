"""cloudj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import website.routes.upload as upload
import website.routes.index as index
import website.routes.mypic as mypic
import website.routes.share as share
import website.routes.download as download
import website.routes.picshow as picshow
import website.routes.delete as delete
import website.routes.login as login
import website.routes.logout as logout
import website.routes.signup as signup
import website.routes.getIV as getIV
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^mypic/', mypic.my_view),
    url(r'^share/', share.my_view),
    url(r'^dl/',download.my_view),
    url(r'^pic/',picshow.my_view),
    url(r'^del/',delete.my_view),
    url(r'^login',login.my_view),
    url(r'^logout',logout.my_view),
    url(r'^signup',signup.my_view),
    url(r'^upload',upload.my_view),
    url(r'^getIV',getIV.my_view),
    url(r'^$', index.my_view),
]