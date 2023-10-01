from django.urls import path
from . import views as quiz_views

urlpatterns = [
    path(r'^&', quiz_views.qpage),
]