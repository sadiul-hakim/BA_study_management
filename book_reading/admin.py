from django.contrib import admin
from .models import Book, Chapter, ReadingProgress, Course, Exam, Improve, ReadingPlan, Revise

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
    list_display = ("book", "chapter", "model", "current_page", "reading_model",
                    "is_completed", "finish_around")
    list_filter = ("is_completed",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Improve)
class ImproveAdmin(admin.ModelAdmin):
    list_display = ("course", "book")
    list_filter = ("course",)
    search_fields = ("course__name", "book__title")


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ("name", "course", "exam_date")
    list_filter = ("course",)


@admin.register(ReadingPlan)
class ReadingPlanAdmin(admin.ModelAdmin):
    list_display = ("course", "book", "chapter", "start_around", "note")
    list_filter = ("course", "book")
    search_fields = ("course__name", "book__title", "note")


@admin.register(Revise)
class ReviseAdmin(admin.ModelAdmin):
    list_display = ("book", "chapter", "possible_date", "note")
    list_filter = ("book",)
    search_fields = ("book__title", "note")
