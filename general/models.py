from django.db import models
from book_reading.models import Book
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.


class StudyNote(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    page = models.IntegerField(default=0)
    note = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.book} - Page {self.page}"


class Notes(models.Model):
    note = CKEditor5Field('Note', config_name='default')

    def __str__(self):
        return self.note[:50]
