from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('simulation/', views.simulation, name='simulation'),
    path('simulation/converse/', views.converse, name='converse'),
    #path('simulation/watson/', views.watson, name='watson')
]
