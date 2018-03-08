from django.shortcuts import render
from django.http import HttpResponse
from django.core.management import call_command
from django.views.decorators.csrf import csrf_exempt
from watson_developer_cloud import ConversationV1
import json
#import watson

conversation = ConversationV1(
	username = 'a2f2135d-5741-4364-803b-66b8116a9b5f',
	password = 'ldTcfTljOKKr',
	version = '2017-05-26'
)
workspace_id = '225a20b1-c3c2-429b-87ba-b389eefc8853'

context = {}

#watson_state = 0
#extrac = ""

# Create your views here.
def index(request):
    return render(request, 'home.html')

def simulation(request):
	user_input = ''
	global context
	response = conversation.message(
	    workspace_id=workspace_id,
	    input={'text': user_input},
	    context = context
	)

	context = response['context']

	return render(request, 'simulation.html',{'response': json.dumps(response['output']['text'][0],indent=2)})

def converse(request):
	global context
	response = conversation.message(
	    workspace_id=workspace_id,
	    input={'text': request.GET.get('user_input')},
	    context = context
	)

	context = response['context']
	
	return HttpResponse(json.dumps(response['output']['text'][0],indent=2))
'''
def watson(request):
	global watson_state
	global extrac
	if(watson_state ==0):
		response, extrac = watson.ask_watson(request.GET.get('user_input'))
		watson_state = 1
	elif(watson_state ==1):
		success, response = watson.ask_watson_response(user_input, extrac)
		if(success != 0):
			watson_state = 0

	return HttpResponse(response)
'''