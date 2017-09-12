from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import bcrypt, re, time
from datetime import date
from bcrypt import hashpw
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
 def register(self, postData):
     error_msgs = []
     try:
         if User.objects.get(username=postData['username']):
             error_msgs.append("Username already in use")
     except:
         pass
     if len(postData['username']) < 3:
         error_msgs.append("Username is too short")
     if len(postData['password']) < 8:
         error_msgs.append("Password is too short")
     if not postData['password'] == postData['confirm']:
         error_msgs.append("Passwords do not match!")
     if error_msgs:
         return {'errors':error_msgs}
     else:
         hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
         user = User.objects.create(username=postData['username'], password=hashed)
         return {'theuser':user.username, 'userid': user.id}
 def login(self, postData):
    error_msgs = []
    password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
    try:
         user = User.objects.get(username=postData['username'])
    except:
        error_msgs.append("Invalid Login Credentials!")
        return {'errors': error_msgs}
    if not bcrypt.hashpw(postData['password'].encode(), user.password.encode()) == user.password.encode():
        error_msgs.append("Incorrect password.")
    if error_msgs:
        return {'errors':error_msgs}
    else:
        return {'theuser':user.username, 'userid':user.id}
class TourdatesManager(models.Manager):
    def addtourdate(self, postData):
        error_msgs = []
        # current_date = time.strftime('%Y-%m-%d')
        if len(postData['tourcity']) < 1:
            error_msgs.append("You need to add a tour city!")
        if len(postData['tourvenue']) <1:
            error_msgs.append("You need to add a tour venue!")
        if len(postData['tourinfourl']) <1:
            error_msgs.append("You need to add a url!")
        if postData['tourdatetime'] < current_date:
            error_msgs.append("You must enter a future start date!")
        if error_msgs:
            return{'errors':error_msgs}
        else:
            tourdateall = Tourdate.objects.create(tourdatetime=postData['tourdatetime'], tourcity=postData['tourcity'], tourvenue=postData['tourvenue'], tourinfourl=postData['tourinfourl'])
            return {'Tourdateid':tourdateall.id}
    def deletetourdate(self, id):
		Tourdate.objects.get(id=id).delete()
                print id

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tourdate(models.Model):
    tourdatetime = models.DateTimeField()
    tourcity = models.CharField(max_length=25)
    tourvenue = models.CharField(max_length=25)
    tourinfourl = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TourdatesManager()
