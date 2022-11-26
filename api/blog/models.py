from secrets import choice
from django.db import models

# Create your models here.
class Blog(models.Model):
    CHOICES     =(("0","Category 1"),("1","Category 2"),("2","Category 3"))
    title       = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    category    = models.CharField(choices=CHOICES, max_length=2)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']