from django import forms

from ..types.image import IMAGE_CLASSIFICATION


class FileUploadForm(forms.Form):
  file = forms.ImageField(
    label='Choose an image',
    widget=forms.FileInput(attrs={'id': 'file_input'})
  )
  image_classification = forms.ChoiceField(
    label='Select Image Classification',
    choices=IMAGE_CLASSIFICATION,
  )

  def clean_file(self):
    file = self.cleaned_data.get('file')

    if file:
      if not file.content_type.startswith('image'):
        raise forms.ValidationError('The file must be an image.')

    return file
