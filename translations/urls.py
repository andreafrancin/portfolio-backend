from django.urls import path
from translations.views import TranslationView

urlpatterns = [
    path('translations/', TranslationView.as_view(), name='translations-list'),
]
