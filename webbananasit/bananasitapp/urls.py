from django.urls import path
from . import views
from .admin import ResumeDownloadAdmin

urlpatterns = [
    path('', views.index, name='IndexPage'),
    path('about/', views.about, name='AboutPage'),
    path('jobapplication/', views.JobApplication.as_view(), name='JobApplicationFormPage'),
    path('admin/documents/<int:object_id>/view/', ResumeDownloadAdmin.view_document_view, name='view_document'),
    path('admin/documents/<int:object_id>/download/', ResumeDownloadAdmin.download_document_view, name='download_document'),
]