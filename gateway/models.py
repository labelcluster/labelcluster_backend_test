from django.db import models
from django.utils import timezone
# Create your models here.

class Gateway(models.Model):

    app_id = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    timestamp = models.CharField(max_length=100)
    sign = models.CharField(max_length=500)
    sign_type = models.CharField(max_length=10)
    encrypt_type = models.CharField(max_length=10)
    biz_data = models.TextField()