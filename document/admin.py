from django.contrib import admin
from .models import Document, DocumentFile
from django.utils.html import format_html
# Register your models here.


class DocumentFileInline(admin.TabularInline):
    model = DocumentFile
    readonly_fields = ("download_link",)
    fields = ("file", "download_link")

    def download_link(self, obj):
        if obj.pk and obj.file:
            return format_html(
                '<a href="{}" target="_blank">Open</a>',
                obj.file.url
            )
        return "-"


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    inlines = [DocumentFileInline]
