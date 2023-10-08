from django.urls import path, re_path
from . import views as quiz_views

urlpatterns = [
    path('<slug:slug>/', quiz_views.qpage, name='quiz'),
]