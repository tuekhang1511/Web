from django.db import models
# from core.models import User
from coding import settings

# from item.models import Item

# Create your models here.
class Lesson(models.Model):
    identification = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)
    def __str__(self):
        return self.name 
