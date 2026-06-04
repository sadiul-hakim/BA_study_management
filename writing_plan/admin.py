from django.contrib import admin

from .models import WritingPlan
# Register your models here.


@admin.register(WritingPlan)
class WritingPlanAdmin(admin.ModelAdmin):
    list_display = ("book", "chapter", "possible_date", "note")
    list_filter = ("book",)
    search_fields = ("book__title", "note")
