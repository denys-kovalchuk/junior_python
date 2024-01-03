from django.urls import path
from .views import get_elements


urlpatterns = [
    path('get_elements/', get_elements, name='get_elements'),
]
