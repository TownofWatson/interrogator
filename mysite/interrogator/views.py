from django.shortcuts import render
from django.http import HttpResponse
from django.core.management import call_command
from django.views.decorators.csrf import csrf_exempt
from watson_developer_cloud import ConversationV1
from django.templatetags.static import static
import os.path
import json
from watson import *
conversation = ConversationV1(
	username = 'a2f2135d-5741-4364-803b-66b8116a9b5f',
	password = 'ldTcfTljOKKr',
	version = '2017-05-26'
)
workspace_id = '225a20b1-c3c2-429b-87ba-b389eefc8853'

context = {}

watson_state = 0
extrac = []

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
