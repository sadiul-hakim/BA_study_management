from django.contrib import admin
from .models import Book, Chapter, ReadingProgress, Course, ReadingPlan, Revise, OtherStudyProgress

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
                    "is_completed", "is_postponed", "finish_around")
    list_filter = ("book", "is_completed", "is_postponed")


@admin.register(OtherStudyProgress)
class OtherStudyProgressAdmin(admin.ModelAdmin):
    list_display = ("topic_name", "note")
    search_fields = ("topic_name",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ReadingPlan)
class ReadingPlanAdmin(admin.ModelAdmin):
    list_display = ("course", "book", "chapter",
                    "start_around", "priority", "order", "note")
    list_filter = ("course", "book", "priority")
    search_fields = ("course__name", "book__title", "note")


@admin.register(Revise)
class ReviseAdmin(admin.ModelAdmin):
    list_display = ("book", "chapter", "possible_date",
                    "priority",  "order", "note")
    list_filter = ("book", "priority",)
    search_fields = ("book__title", "note")
