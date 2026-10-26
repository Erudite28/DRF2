from django.urls import path
from .views import singleobject, multipleobject

urlpatterns = [
    path('singleobj/', singleobject, name='single_object'),
    path('multipleobj/', multipleobject, name='multiple_object'), 
]