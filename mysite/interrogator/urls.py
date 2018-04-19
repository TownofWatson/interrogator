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
    path('simulation/converse_person_change/', views.converse_person_change, name='converse_person_change'),
    path('simulation/guess_suspect/', views.guess_suspect, name='guess_suspect'),
    path('simulation/get_speech/', views.get_speech, name='get_speech'),
    path('simulation/speak/', views.speak, name='speak'),
    path('simulation/speak_switch/', views.speak_switch, name='speak_switch'),
    path('simulation/change_language/', views.change_language, name='change_language'),
    path('simulation/watson_button_length/', views.watson_button_length, name='watson_button_length'),
    path('simulation/translate_input/', views.translate_input, name='translate_input'),
    path('simulation/translate_output/', views.translate_output, name='translate_output'),

]
