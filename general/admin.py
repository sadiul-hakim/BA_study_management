from django.contrib import admin
from .models import Notes

# Register your models here.


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ("note",)
    search_fields = ("note",)

    def has_module_permission(self, request):
        self.model._meta.verbose_name_plural = "Notes"
        return super().has_module_permission(request)
