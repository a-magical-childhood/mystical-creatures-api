# Create your views here.
from django.shortcuts import render
from rest_framework import generics
 
from .models import Creatures
from .serializers import CreaturesSerializer

class CreaturesList(generics.ListCreateAPIView):
  queryset = Creatures.objects.all()
  serializer_class = CreaturesSerializer
 
class Sightings(generics.RetrieveUpdateDestroyAPIView):
  queryset = Creatures.objects.all()
  serializer_class = CreaturesSerializer
