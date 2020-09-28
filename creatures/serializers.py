from rest_framework import serializers
from .models import Creatures

class CreaturesSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id','creature_name','latitude', 'longitude', 'description','explorer')
    model = Creatures


