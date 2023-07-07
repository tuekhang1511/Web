from django.db import models
from lessons.models import Lesson

# Create your models here.


class TryCode(models.Model):
    in_lesson = models.ForeignKey(Lesson, blank=True,null=True, related_name='trycode', on_delete=models.CASCADE)
    intro = models.TextField(max_length=1000, default='')
    description = models.TextField(max_length=1000, default='')
    detail = models.TextField(blank=True,null=True)
    # def __str__(self):
    #     return self.name 