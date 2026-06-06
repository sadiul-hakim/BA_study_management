from django.db import models

# Create your models here.


class Notes(models.Model):
    note = models.TextField(max_length=300)
