from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('simulation/', views.simulation, name='simulation'),
    path('simulation/converse/', views.converse, name='converse'),
    path('simulation/watson/', views.watson, name='watson'),
    path('simulation/watson_button_label/', views.watson_button_label, name='watson_button_label'),
    path('simulation/watson_button/', views.watson_button, name='watson_button'),
    path('simulation/watson_button_respond/', views.watson_button_respond, name='watson_button_respond'),

    path('simulation/watson_button_length/', views.watson_button_length, name='watson_button_length')

]
