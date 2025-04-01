from django.contrib import admin
from translations.models import Translation

# Register your models here.
@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_en', 'text_es', 'text_ca')
    search_fields = ('id', 'text_en', 'text_es', 'text_ca')