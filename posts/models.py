from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table = 'post'
    name = models.CharField(
        'Name' , blank = False,null = False ,max_length = 14 , db_index = True ,default = 'Anonymous'
    )
    body = models.CharField(
        'Body' , blank = True , null = True ,max_length = 140 , db_index = True
    )
    created_at = models.DateTimeField(
        'Created Datetime' , blank = True, auto_now_add = True
    )
    likes = models.IntegerField(
        'likes' , default = 0 , blank=True
    )
    image = CloudinaryField(
        'image' , blank = True, db_index= True
    )