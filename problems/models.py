from django.db import models

# Create your models here.
from coding import settings
from lessons.models import Lesson

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

# Create your models here.
class Problem(models.Model):
    category = models.ForeignKey(Category, related_name='problems', on_delete=models.CASCADE)
    in_lesson = models.ForeignKey(Lesson, blank=True,null=True, related_name='problems', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    problem_description = models.TextField(blank=True,null=True)
    word_in_solution_code = models.TextField(blank=True,null=True)
    hint = models.TextField(blank=True,null=True, default='')
    result = models.TextField(blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.name 