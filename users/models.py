from django.db import models
from django.contrib.auth.models import User
from PIL import Image
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image= models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __Str__(self):
        return f'{self.user.username} Profile'
    
    # models.py
from PIL import Image
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username}'s Profile"

   # You can lower quality for smaller size
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img_path = self.image.path
        img = Image.open(img_path)

        # Resize image if it's too large
        max_size = (300, 300)
        if img.height > 300 or img.width > 300:
            img.thumbnail(max_size)

        # Save it with optimized quality
        img.save(img_path, format='JPEG', quality=70)



    




