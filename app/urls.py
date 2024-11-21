from django.views.generic import TemplateView
from django.urls import path

from .views import upload

urlpatterns = [
  path('', TemplateView.as_view(template_name='index.html'), name='index'),
  path('upload/', upload.upload_file, name='upload'),
]
