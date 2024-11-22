
import logging
from django.http import JsonResponse
from django.shortcuts import render

from ..models.image import ImageModel
from ..forms.upload import FileUploadForm
from ..ai.image import classify_image

logger = logging.getLogger(__name__)


def upload_file(request):
  if request.method == 'POST':
    form = FileUploadForm(request.POST, request.FILES)

    if form.is_valid():
      try:
        file = form.cleaned_data['file']
        predictions = classify_image(file)

        ImageModel(
          file_data=file.read(),
          file_name=file.name,
          image_type=file.content_type,
          provided_image_classification=form.cleaned_data['image_classification'],
          predicted_image_classification=[
            {
              'class_name': class_name,
              'score': score
            } for class_name, score in predictions
          ]
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


def get_list(_):
  documents = ImageModel.objects.values(
    'file_name',
    'provided_image_classification',
    'predicted_image_classification',
  )

  return JsonResponse(list(documents), safe=False)
