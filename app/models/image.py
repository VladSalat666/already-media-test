from djongo import models

from ..models.prediction import Prediction
from ..types.image import IMAGE_CLASSIFICATION


class ImageModel(models.Model):
  file_data = models.BinaryField()
  file_name = models.CharField(max_length=50)
  image_type = models.CharField(max_length=50)
  provided_image_classification = models.CharField(choices=IMAGE_CLASSIFICATION, max_length=50)
  predicted_image_classification = models.ArrayField(model_container=Prediction)

  class Meta:
    db_table = 'images'

  def __str__(self):
    return f'Image {self.file_name} saved'
