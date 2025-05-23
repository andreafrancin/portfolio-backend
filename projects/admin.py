from django.contrib import admin
from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_en', 'type')
    search_fields = ('id', 'type', 'title_en', 'title_es', 'title_ca')
    list_filter = ('type',)
    inlines = [ProjectImageInline]
