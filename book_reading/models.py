from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    PRIORITY_CHOICES = [
        (LOW, "Low"),
        (MEDIUM, "Medium"),
        (HIGH, "High"),
    ]

    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="books")
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=MEDIUM)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="chapters"
    )
    title = models.CharField(max_length=255)
    chapter_number = models.IntegerField()

    def __str__(self):
        return f"{self.book.title} - {self.title}"


class ReadingProgress(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True,
                                blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    current_page = models.IntegerField(default=0)
    model = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    reading_model = models.BooleanField(default=False)

    updated_at = models.DateTimeField(auto_now=True)
    finish_around = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.chapter} - page {self.current_page}"


class ReadingPlan(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True,
                                blank=True)
    note = models.TextField(blank=True)
    start_around = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.course} - {self.book}"


class Revise(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True,
                                blank=True)
    note = models.TextField(blank=True)
    possible_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book} - {self.chapter}"
