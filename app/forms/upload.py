from django import forms

IMAGE_CHOICES = [
  ('food', 'Food'),
  ('nature', 'Nature'),
  ('city', 'City'),
]


class FileUploadForm(forms.Form):
  file = forms.ImageField(
    label='Choose an image',
    widget=forms.FileInput(attrs={'id': 'file_input'})
  )
  image_type = forms.ChoiceField(choices=IMAGE_CHOICES, label='Select Image Type')

  def clean_file(self):
    file = self.cleaned_data.get('file')

    if file:
      if not file.content_type.startswith('image'):
        raise forms.ValidationError('The file must be an image.')

    return file
