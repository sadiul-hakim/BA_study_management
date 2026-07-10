from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class DocumentFile(models.Model):
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name="files"
    )

    file = models.FileField(
        upload_to="documents/"
    )

    def __str__(self):
        return self.file.name
