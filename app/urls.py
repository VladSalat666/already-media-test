from django.views.generic import TemplateView
from django.urls import path

from . import views

urlpatterns = [
  path('', TemplateView.as_view(template_name="index.html"), name='index'),
  path('handle_form/', views.handle_form, name='handle_form'),
]
