from django.urls import path
from .views import CreaturesList, Sightings

urlpatterns = [
  path('', CreaturesList.as_view(), name="creatures"),
  path('sightings/<int:pk>/', Sightings.as_view(), name="sightings"),
]
