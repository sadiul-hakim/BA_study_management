from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.title


class ReadingProgress(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reading_page = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    is_postponed = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    finish_around = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book} - page {self.reading_page}"


class ReadingPlan(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    note = models.TextField(blank=True)
    start_around = models.DateField(null=True, blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.book} - {self.book}"


class StudyNote(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    page = models.IntegerField(default=0)
    note = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.book} - Page {self.page}"


class Lend(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    receiver = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    return_date = models.DateField(auto_now=True)
