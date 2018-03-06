from django.shortcuts import render
from watson_developer_cloud import ConversationV1
import json

# Create your views here.
def index(request):
    return render(request, 'home.html')

def simulation(request):
	conversation = ConversationV1(
	username = 'a2f2135d-5741-4364-803b-66b8116a9b5f',
	password = 'ldTcfTljOKKr',
	version = '2017-05-26'
	)
	workspace_id = '225a20b1-c3c2-429b-87ba-b389eefc8853'

	context = {}
	user_input = ''
	response = conversation.message(
	    workspace_id=workspace_id,
	    input={'text': user_input},
	    context = context
	)

	context = response['context']
	conversation = {'response': json.dumps(response['output']['text'][0],indent=2)}

	return render(request, 'simulation.html',conversation)
