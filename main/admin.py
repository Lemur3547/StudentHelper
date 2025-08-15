from django.contrib import admin
from main.models import AttachedFile, Subject, Material, Solution

# Register your models here.
admin.site.register(Subject)
admin.site.register(Material)
admin.site.register(Solution)

@admin.register(AttachedFile)
class AttachedFileAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "object_name", "content_type")

    def object_name(self, obj):
        return str(obj.content_object)
