from django.views.generic import TemplateView
from django.urls import path

from .views import image

urlpatterns = [
  path('', TemplateView.as_view(template_name='index.html'), name='index'),
  path('upload/', image.upload_file, name='upload'),
  path('images/', image.get_list, name='images-list'),
]
