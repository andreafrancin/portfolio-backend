from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from translations.models import Translation
from translations.serializers import TranslationSerializer

class TranslationView(APIView):
    """
    API endpoint to retrieve all translations.
    """
    def get(self, request):
        lang = request.headers.get('Accept-Language', 'en')[:2]

        translations = Translation.objects.all()

        serializer = TranslationSerializer(translations, many=True, context={"language": lang})
        print(serializer)
        return Response(serializer.data)