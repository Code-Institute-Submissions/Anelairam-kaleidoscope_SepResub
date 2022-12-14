from django.urls import path
from . import views

urlpatterns = [
    path('', views.eshop, name='eshop'),
    path('tutorials/', views.tutorials, name='tutorials'),
    path('add_tutorial/', views.add_tutorial, name='add_tutorial'),
    path('edit/<int:tutorial_id>/', views.edit_tutorial, name='edit_tutorial'),
    path('delete/<int:tutorial_id>/', views.delete_tutorial, name='delete_tutorial'),
]