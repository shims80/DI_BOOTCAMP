from django.urls import path
from . import views
urlpatterns = [
	path('', views.home, name='home'),
    path('animal/<int:animal_id>', views.animal,name='animal'),
    path('family/<int:family_id>', views.family,name='family'),
]

