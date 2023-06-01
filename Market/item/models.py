from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User



class category(models.Model):

    name = models.CharField(max_length=20)

    class Meta:
        
        ordering = ('name',)
        verbose_name_plural = ('Catergories')

    def __str__(self):
        return self.name



class item(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank = True,null = True)
    price = models.IntegerField()
    categ = models.ForeignKey(category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='item_images/',blank = True, null = True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    sold = models.BooleanField(default=False)

    class Meta:
        
        ordering = ('name',)
        

    def __str__(self):
        return self.name