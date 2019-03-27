from django.db import models

# Create your models here.

from django.db import models
from tinymce.models import HTMLField


# Create your models here.


class profile(models.Model):
    image= models.CharField(max_length =30)
    name = models.CharField(max_length =30)
    bio = models.CharField(max_length =30)
    def __str__(self):
        return self.country



    
class Comments(models.Model):
    name  = models.CharField(max_length =30)
    bio = models.CharField(max_length =30)
    def __str__(self):
        return self.name


    @classmethod
    def search_by_category(cls,name):
        category = cls.objects.filter(image_name__icontains=image_name).first()
        images=Image.objects.filter(category=category)
        return images
     
class Follow(models.Model):
    name= models.CharField(max_length =30)
    bio = models.CharField(max_length =30) 
    def __str__(self):
        return self.name





class Image(models.Model):
    image = models.CharField(max_length =30)
    picture = models.ImageField(upload_to='photo/') 
    like= models.TextField()
    # location = models.ForeignKey(Location)
    # category = models.ForeignKey(Category)
    def __str__(self):
        return self.image
