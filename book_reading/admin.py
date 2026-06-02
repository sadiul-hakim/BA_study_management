from django.contrib import admin
from .models import Book, Chapter, ReadingProgress, Course, Exam

# Register your models here.

# setting
admin.site.site_header = "BA Study Tracker"
admin.site.site_title = "Study Tracker"
admin.site.index_title = "Dashboard"

# Models


class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "priority")
    list_filter = ("priority", "course")
    search_fields = ("title",)

    inlines = [ChapterInline]


@admin.register(ReadingProgress)
class ReadingProgressAdmin(admin.ModelAdmin):
    list_display = ("chapter", "model", "current_page", "reading_model",
                    "is_completed", "updated_at")
    list_filter = ("is_completed",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ("name", "course", "exam_date")
    list_filter = ("course",)
