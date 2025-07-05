from django.urls import path
from . import views

urlpatterns = [
    path('generate-cv/', views.generate_cv, name='generate_cv'),
    path('health/', views.health_check, name='health_check'),
]