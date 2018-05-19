from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<User Object: {} {} {} {} {}>".format(self.first_name, self.last_name, self.email, self.created_at,self.updated_at)



class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploader = models.ForeignKey(User, related_name="uploaded_books")
    liked_users = models.ManyToManyField(User, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Book Object: {} {} {} {} {} {}>".format(self.title, self.desc, self.uploader, self.liked_users, self.created_at, self.updated_at)

   