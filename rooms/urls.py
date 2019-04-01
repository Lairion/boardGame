from django.urls import path,include 
from rest_framework_swagger.views import get_swagger_view
from .views import RoomViews

urlpatterns = [
    path('rooms/', RoomViews.list_view ),
]
