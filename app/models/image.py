from djongo import models

from app.types.image import IMAGE_TYPE


class ImageModel(models.Model):
  file_data = models.BinaryField()
  file_name = models.CharField(max_length=50)
  image_type = models.CharField(choices=[item[0] for item in IMAGE_TYPE])

  class Meta:
    db_table = 'images'

  def __str__(self):
    return f'Image {self.image_type} saved'
