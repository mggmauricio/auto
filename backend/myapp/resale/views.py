from rest_framework import generics
from .serializers import VehicleSerializer
from .models import Category, Manufacter, Vehicle, CategoryCosts, Costs

# Create your views here.


class ListVehicle(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class DetailVehicle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer