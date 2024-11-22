from djongo import models


class Prediction(models.Model):
  class_name = models.CharField(max_length=50)
  score = models.FloatField()

  class Meta:
    abstract = True
