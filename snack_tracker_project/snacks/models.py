from django.db import models
from django.contrib.auth import get_user_model

class Snack(models.Model):
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=64, null= True, blank=True)
    description = models.TextField()
    