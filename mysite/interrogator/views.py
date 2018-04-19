from django.shortcuts import render
from django.http import HttpResponse
from django.core.management import call_command
from django.views.decorators.csrf import csrf_exempt
from watson_developer_cloud import ConversationV1
from watson_developer_cloud import LanguageTranslatorV2
from django.templatetags.static import static
import os.path
import json
from testspeech import *
from watson import *
import speech_recognition as sr

conversation = ConversationV1(
	username = 'a2f2135d-5741-4364-803b-66b8116a9b5f',
	password = 'ldTcfTljOKKr',
	version = '2017-05-26'
)

language_translator = LanguageTranslatorV2(
  username= 'd983f17b-f4dc-4af1-baec-d6bebd118ef1',
  password= 'WpeErdZeiPXZ',
  url= 'https://gateway.watsonplatform.net/language-translator/api'
)

workspace_id = '225a20b1-c3c2-429b-87ba-b389eefc8853'

context = {}
speaking = True
watson_state = 0
extrac = []
language = 'en'

# Create your views here.
def index(request):
    return render(request, 'home.html')

def simulation(request):
	user_input = ''
	global context
	response = conversation.message(
	    workspace_id=workspace_id,
	    message_input={'text': user_input},
	)

	context = response['context']

	return render(request, 'simulation.html',{'response': json.dumps(response['output']['text'][0],indent=2)})

def converse(request):
	global context
	response = conversation.message(
	    workspace_id=workspace_id,
	    message_input={'text': request.GET.get('user_input')},
	    context = context,
	)

	context = response['context']

	return HttpResponse(json.dumps(response['output']['text'][0],indent=2)[1:-1])

def converse2(request):
	global context
	response = conversation.message(
	    workspace_id=workspace_id,
	    message_input={'text': request},
	    context = context,
	)

	context = response['context']

	return (json.dumps(response['output']['text'][0],indent=2)[1:-1])


def change_language(request):
	global language
	language = request.GET.get('user_input')
	return HttpResponse()

def speak(request):
	global speaking
	global language
	read = request.GET.get('user_input')
	if(read.find(':') != -1 and speaking == True):
		speak_text(read[read.find(':'):], language)

	return HttpResponse()

def speak_switch(request):

	global speaking
	speaking = not speaking

	return HttpResponse()

def converse_person_change(request):
	name = request.GET.get('user_input')
	return("yes")

def guess_suspect(request):
	guess = request.GET.get('user_input')
	final_message = ""
	if guess.lower() == 'gabriella fresquez' or guess.lower() == 'gabriella':
		final_message = "Congratulations! You successfully apprehended the criminal, Gabriella Fresquez."
	else:
		final_message = guess.upper() + " is not the culprit! You've convicted an innocent while the real criminal disappeared without a trace.\n Press 'restart' to try again."
	return HttpResponse(final_message)


def watson(request):
	global watson_state
	global extrac
	# if(watson_state ==0):
	# 	response, extrac = ask_watson(request.GET.get('user_input'))
	# 	watson_state = 1
	# elif(watson_state ==1):
	# 	success, response = ask_watson_response(request.GET.get('user_input'), extrac)
	# 	if(success != 0):
	# 		watson_state = 0

	response, extrac = ask_watson(request.GET.get('user_input'))

	return HttpResponse(response)

def translate_input(request):
	sentence=request.GET.get('user_input')

	global language
	print(language)
	print(sentence)
	translation = ""

	if language == 'es':
	    	translation = language_translator.translate(text=sentence,model_id="es-en")
	if language == 'fr':
			translation = language_translator.translate(text=sentence,model_id="fr-en")
	if language == 'ja':
	 	       translation = language_translator.translate(text=sentence,model_id="ja-en")
	if language == 'ko':
	        	translation = language_translator.translate(text=sentence,model_id="ko-en")
	if language == 'en':
			translation = sentence

	print(translation)
	return HttpResponse(translate_output(converse2(translation)))

def translate_output(request):
	sentence=request

	global language
	print(language)
	print(sentence)
	translation = ""

	if language == 'es':
	    	translation = language_translator.translate(text=sentence,model_id="en-es")
	if language == 'fr':
			translation = language_translator.translate(text=sentence,model_id="en-fr")
	if language == 'ja':
	 	       translation = language_translator.translate(text=sentence,model_id="en-ja")
	if language == 'ko':
	        	translation = language_translator.translate(text=sentence,model_id="en-ko")
	if language == 'en':
			translation = sentence

	print(translation)
	#afterSpeak = speak(translation)
	#print(afterSpeak)
	return translation

def watson_button_label(request):
	return HttpResponse(extrac[int(request.GET.get('user_input'))])

def watson_button_length(request):
	return HttpResponse(len(extrac))

def watson_button_respond(request):
	path = 'pdfs/gen/'+str(request.GET.get('user_input'))
	#print_to_html(path)
	return HttpResponse("/static/"+path)

def watson_button(request):
	success, response = ask_watson_response(request.GET.get('user_input'), extrac)
	return HttpResponse(response)

def get_speech(request):
	# get language
	lang_code = request.GET.get('language')
	global language
	if language == 'es':
		lang_code = 'es-ES'
	if language == 'fr':
		lang_code = 'fr-FR'
	if language == 'ja':
		lang_code = 'ja-JP'
	if language == 'ko':
		lang_code = 'ko-KR'

	time_to_speech = 5
	time_of_speech = 10
	# obtain audio from the microphone
	r = sr.Recognizer()
	r.adjust_for_ambient_noise
	r.pause_threshold = 0.5
	with sr.Microphone() as source:
	    audio = r.listen(source,time_to_speech,time_of_speech)

	# recognize speech using IBM Speech to Text
	try:
	    response = r.recognize_ibm(audio, username="f7439e9c-7d03-4c96-8fa7-cb792aeaa846", password="bTiV7BUg8ShR",language=lang_code)
	except sr.UnknownValueError:
	    response = "IBM Speech to Text could not understand audio"
	except sr.RequestError as e:
		response = "Could not request results from IBM Speech to Text service; {0}".format(e)

	return HttpResponse(response)
