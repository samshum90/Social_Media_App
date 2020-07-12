from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    dob = models.DateField()
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone_no = models.IntegerField()
    join_date = models.DateTime(auto_now_add=True, blank=True)

class Authentication(models.Model):
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Interest(models.Model):
    movie = models.CharField(max_length=255)
    music = models.CharField(max_length=255)
    human_rights = models.CharField(max_length=255)
    world_topics = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Post(models.Model):
    content = models.CharField(max_length=255)
    post_date = models.DateTime(auto_now_add=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Buddy(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, on_delete=models.CASCADE)
    buddy_date = models.DateTime(auto_now_add=True, blank=True)


class Following(model.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    follow_date = models.DateTimeField(auto_now_add=True, blank=True)