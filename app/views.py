
from django.shortcuts import redirect, render

from .forms.upload import FileUploadForm


def index(request):
  return render(request, 'index.html', name='index')


def upload_file(request):
  if request.method == 'POST':
    form = FileUploadForm(request.POST, request.FILES)

    if form.is_valid():
      # uploaded_file = form.cleaned_data['file']
      # image_type = form.cleaned_data['image_type']

      return redirect('index')
  else:
    form = FileUploadForm()

  return render(request, 'upload.html', {'form': form})
