from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Dataset(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="datasets/")

class Variable(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)  # e.g., 'numerical', 'categorical'
    label = models.CharField(max_length=255, blank=True)
    missing_values = models.JSONField(default=list, blank=True)
    value_labels = models.JSONField(default=dict, blank=True)