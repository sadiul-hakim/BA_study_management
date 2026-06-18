from django.db import models
from book_reading.models import Book
# Create your models here.


class StudyNote(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    page = models.IntegerField(default=0)
    note = models.TextField(max_length=500)


class Notes(models.Model):
    note = models.TextField(max_length=500)
