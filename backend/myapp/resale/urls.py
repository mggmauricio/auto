from django.urls import path
from .views import ListVehicle, DetailVehicle


urlpatterns = [
    path('<int:pk>/',  DetailVehicle.as_view()),
    path('', ListVehicle.as_view()),

]