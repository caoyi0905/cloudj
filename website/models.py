from __future__ import unicode_literals


from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Picture(models.Model):
    picture_name=models.CharField(max_length=30)
    key=models.CharField(max_length=16)
    IV=models.CharField(max_length=16)
    filled=models.IntegerField()
    onner=models.ForeignKey(User,related_name='username_set')
    isshared=models.BooleanField(default=False)

    def __str__(self) :
        return self.picture_name
