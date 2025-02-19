from django.urls import path
from . import views

urlpatterns = [
    path('', views.simulation_view, name='simulation'),
    path('move/', views.move_point, name='move_point'),  # URL pour déplacer le point rouge
]
