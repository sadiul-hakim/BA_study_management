from django.db import models

from book_reading.models import Book, Chapter

# Create your models here.


class WritingPlan(models.Model):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    PRIORITY_CHOICES = [
        (LOW, "Low"),
        (MEDIUM, "Medium"),
        (HIGH, "High"),
    ]

    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=MEDIUM)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True,
                                blank=True)
    note = models.TextField(blank=True)
    possible_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book} - {self.chapter}"
