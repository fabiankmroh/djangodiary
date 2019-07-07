from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:entry_id>', views.detail, name='detail'),
    path('<int:entry_id>/save', views.save, name='save'),
]