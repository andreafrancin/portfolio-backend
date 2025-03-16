from rest_framework import serializers
from .models import Project, ProjectImage

class ProjectImageSerializer(serializers.ModelSerializer):
    """
    Serializer for project images.
    """
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProjectImage
        fields = ['image_url']

    def get_image_url(self, obj):
        # Construct the full URL for the image
        return f"https://res.cloudinary.com/dzitjg3qy/{obj.image}"

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
