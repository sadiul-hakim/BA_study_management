from django.contrib import admin
from .models import Notes, StudyNote

# Register your models here.


@admin.register(StudyNote)
class StudyNoteAdmin(admin.ModelAdmin):
    list_display = ("book", "page", "note")
    search_fields = ("book", "note",)
    list_filter = ("book",)


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ("note",)
    search_fields = ("note",)

    def has_module_permission(self, request):
        self.model._meta.verbose_name_plural = "Notes"
        return super().has_module_permission(request)
