from django.urls import path
from . import views
 
urlpatterns = [
    path('animals/',views.all_animals )
]
