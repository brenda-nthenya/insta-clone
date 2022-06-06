from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts')
    caption = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.author.username} post'

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='', upload_to='profile_pics')
    profile_caption = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.username} Profile'
