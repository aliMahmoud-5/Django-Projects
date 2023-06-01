from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class posts(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    date = models.DateField(default=timezone.now)
    auth = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})