from django.urls import path
from . import views

urlpatterns = [
    path('', views.site),
    path('about/<str:myname>', views.about),
]