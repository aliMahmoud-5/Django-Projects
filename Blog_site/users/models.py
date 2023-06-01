from django.db import models
from django.contrib.auth.models import User
#from PIL import Image

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(default='profile_pics/default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

    #def save(self):
        super().save()

        pict = Image.open(self.pic.path)
        
        if pict.width > 300 or pict.height > 300:
            output_size = (300,300)
            pict.thumbnail(output_size)
            pict.save(self.pic.path)