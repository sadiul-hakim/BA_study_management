from django.db import models


class Guide(models.Model):
    text = models.TextField()
    priority = models.IntegerField(default=0)

    class Meta:
        ordering = ['priority']

    def __str__(self):
        return f"Guide {self.priority}"
