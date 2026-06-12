from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#this class will represent a tweet, it will have the one-one relationship with the user mode,
class Tweet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=280)
    photo = models.ImageField(upload_to='tweets/photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # now we will make the dunder method for this class, this method will return the text  of the tweet
    def __str__(self):
        return f'{self.user.username}: {self.text[:50]}'
