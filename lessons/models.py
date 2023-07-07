from django.db import models
# from core.models import User
from coding import settings

# from item.models import Item

# Create your models here.
class Lesson(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    context = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)
    def __str__(self):
        return self.name 
