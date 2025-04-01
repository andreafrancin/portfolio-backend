from rest_framework import serializers
from translations.models import Translation

class TranslationSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField()

    class Meta:
        model = Translation
        fields = ['id', 'key', 'text']

    def get_text(self, obj):
        lang = self.context.get("language", "en")
        return getattr(obj, f"text_{lang}", obj.text_en)
    
    def get_key(self, obj):
        return getattr(obj, f"key", obj.key)