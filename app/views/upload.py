
import logging
from django.shortcuts import render

from ..models.image import ImageModel
from ..forms.upload import FileUploadForm

logger = logging.getLogger(__name__)


def upload_file(request):
  if request.method == 'POST':
    form = FileUploadForm(request.POST, request.FILES)

    if form.is_valid():
      try:
        ImageModel(
          file_data=form.cleaned_data['file'].read(),
          file_name=form.cleaned_data['file'].name,
          image_type=form.cleaned_data['image_type'],
        ).save()

        return render(request, 'upload.html', {
            'form': form,
            'status': 'success',
            'message': 'File successfully uploaded and saved.',
          })
      except Exception as e:
        logger.error("Error while saving file to the database: %s", e)

        return render(request, 'upload.html', {
            'form': form,
            'status': 'error',
            'message': 'Internal Server Error: Could not save the file.',
        })
  else:
    form = FileUploadForm()

  return render(request, 'upload.html', {'form': form})
