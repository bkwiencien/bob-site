from django.db import models

# Create your models here.

class Comments(models.Model):
    comment = models.CharField(max_length=500)
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
