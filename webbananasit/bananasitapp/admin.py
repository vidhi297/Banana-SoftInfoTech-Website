from django.contrib import admin

from django.utils.html import format_html
from django.http import HttpResponse
from django.conf import settings
import os

from .models import AboutU, Service, Portfolio, ContactText, Testimonial, Client, TeamMember, Contact, Faq, SubscriptionId, Resume, JobPost, Slider

# Register your models here.

class ResumeDownloadAdmin(admin.ModelAdmin):
    list_display = ['seeker_name', 'seeker_email', 'view_document', 'download_document']

    def view_document(self, obj):
        return format_html('<a href="{}">View</a>', obj.get_view_url())
    view_document.short_description = 'View'

    def download_document(self, obj):
        return format_html('<a href="{}">Download</a>', obj.get_download_url())
    download_document.short_description = 'Download'
    
    def get_urls(self):
        from django.urls import path

        urls = super().get_urls()
        custom_urls = [
            path('<path:object_id>/view/', self.view_document_view, name='view_document'),
            path('<path:object_id>/download/', self.download_document_view, name='download_document')
        ]
        return custom_urls + urls
    
    def view_document_view(self, request, object_id):
        doc = Resume.objects.get(id=object_id)
        file_path = os.path.join(settings.MEDIA_ROOT, str(doc.seeker_resume))
        print(file_path)

        # Check if the file exists
        if os.path.exists(file_path):
            # For PDF files
            if str(doc.seeker_resume).lower().endswith('.pdf'):
                with open(file_path, 'rb') as f:
                    response = HttpResponse(f.read(), content_type='application/pdf')
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                    return response
            
        # Handling the case where the file doesn't exists
        return HttpResponse('File not found', status=404)
    
    def download_document_view(self, request, object_id):
        doc = Resume.objects.get(id=object_id)
        file_path = os.path.join(settings.MEDIA_ROOT, str(doc.seeker_resume))
        print(file_path)

        # Check if the file exists
        if os.path.exists(file_path):
            # Open file in binary mode
            with open(file_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type='application/octet-stream')
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                return response
            
        # Handling the case where the file doesn't exists
        return HttpResponse('File not found', status=404)

admin.site.register(AboutU)
admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(ContactText)
admin.site.register(Testimonial)
admin.site.register(Client)
admin.site.register(TeamMember)
admin.site.register(Contact)
admin.site.register(Faq)
admin.site.register(SubscriptionId)
admin.site.register(Resume, ResumeDownloadAdmin)
admin.site.register(JobPost)
admin.site.register(Slider)
