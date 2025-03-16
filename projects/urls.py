from django.urls import path
from .views import ProjectDetailView, ProjectListView

urlpatterns = [
    path('project/<int:project_id>/', ProjectDetailView.as_view(), name='project-detail'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
]
