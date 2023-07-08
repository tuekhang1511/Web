from django.db import models
from lessons.models import Lesson

# Create your models here.


class TryCode(models.Model):
    identification = models.IntegerField(default=0)
    in_lesson = models.ForeignKey(Lesson, blank=True,null=True, related_name='trycode', on_delete=models.CASCADE)
    intro = models.TextField(max_length=1000, default='', blank=True,null=True)
    summary = models.TextField(blank=True,null=True, default='')
    detail = models.TextField(blank=True,null=True)
    def __str__(self):
        return str(self.identification) 