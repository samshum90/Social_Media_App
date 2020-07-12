from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    dob = models.DateField()
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone_no = models.IntegerField()
    join_date = models.DateTime()

class Authentication(models.Model):
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Interest(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Post(models.Model):
    content = models.CharField(max_length=255)
    post_date = models.DateTime()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Buddy(models.Model):
    buddy_date = models.DateTime()


class Following(model.Model):
