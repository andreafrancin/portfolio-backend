from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer

class ProjectDetailView(APIView):
    """
    API endpoint to retrieve project details by ID.
    """
    def get(self, request, project_id):
        lang = request.headers.get('Accept-Language', 'en')[:2]

        try:
            project = Project.objects.get(id=project_id)
            serializer = ProjectSerializer(project, context={"language": lang})
            return Response(serializer.data)
        except Project.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

class ProjectListView(APIView):
    """
    API endpoint to retrieve all projects, optionally filtered by type.
    """
    def get(self, request):
        lang = request.headers.get('Accept-Language', 'en')[:2]
        project_type = request.query_params.get('type')

        if project_type:
            projects = Project.objects.filter(type=project_type)
        else:
            projects = Project.objects.all()

        serializer = ProjectSerializer(projects, many=True, context={"language": lang})
        return Response(serializer.data)
