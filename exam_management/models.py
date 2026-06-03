from django.db import models
from book_reading.models import Course, Book

# Create your models here.


class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    exam_date = models.DateField()

    def __str__(self):
        return self.name


class Improve(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course} - {self.book}"
