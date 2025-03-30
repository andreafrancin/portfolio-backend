from rest_framework import serializers
from .models import Project, ProjectImage

class ProjectImageSerializer(serializers.ModelSerializer):
    """
    Serializador for the project images
    """
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProjectImage
        fields = ['image_url']

    def get_image_url(self, obj):
        return obj.image.url

    def create(self, validated_data):
        existing_image = ProjectImage.objects.filter(image=validated_data["image"]).first()
        if existing_image:
            return existing_image

        return super().create(validated_data)


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer to convert Project model instances into JSON format.
    """
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    image_resources = ProjectImageSerializer(many=True, source='images')

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'image_resources']

    def get_title(self, obj):
        lang = self.context.get("language", "en")
        return getattr(obj, f"title_{lang}", obj.title_en)

    def get_description(self, obj):
        lang = self.context.get("language", "en")
        return getattr(obj, f"description_{lang}", obj.description_en)
