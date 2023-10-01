from django.urls import path, re_path
from . import views as quiz_views

urlpatterns = [
    path('', quiz_views.qpage),
]