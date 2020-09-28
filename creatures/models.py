from django.db import models

# Create your models here.

class Creatures(models.Model):
  id = models.IntegerField
  creature_name = models.CharField(max_length=255)
  latitude = models.CharField(max_length=255)
  longitude = models.CharField(max_length=255)
  description = models.TextField(default = "option")
  explorer = models.TextField(default = "option")

  def __str__(self):
    return self.creature_name + self.description