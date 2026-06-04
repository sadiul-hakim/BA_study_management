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


class LiteraryWork(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="works"
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name="works"
    )

    def __str__(self):
        return self.name
