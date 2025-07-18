from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
      return reverse('post-detail', kwargs={'pk': self.pk})

#Test table
class test(models.Model):
   name=models.CharField(max_length=100)
   dummyName=models.CharField(max_length=100,default='Dummy')