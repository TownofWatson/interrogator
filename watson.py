import sys
import os
import json
import time
import webbrowser
import mimetypes
import easygui
import nltk
from textblob import TextBlob
from textblob import Word
from watson_developer_cloud import DiscoveryV1
import random
import ctypes  

response_for_not_knowing = ["Couldn't tell ya, mate", "I'm not quite sure I can answer that.", 
"Well pickle me tender, I've no clue.", "That is a really good question", "Huh",  "You know, there are some questions that even I can't answer",
"My literature doesn't really speak of that"]
discovery = DiscoveryV1(
  username="adbf14e6-bc4b-4f02-a71f-e3914e61f623",
  password="OlSYr70ryMdK",
  version="2017-11-07"
)


environments = discovery.get_environments()
#print(json.dumps(environments, indent=2))

watson_environments = [x for x in environments['environments'] if x['name'] == 'my_environment']
watson_environment_id = watson_environments[0]['environment_id']
#print(json.dumps(watson_environment_id, indent=2))

collections = discovery.list_collections(watson_environment_id)
watson_collections = [x for x in collections['collections']]
#print(json.dumps(collections, indent=2))

watson_collection = watson_collections[0]['collection_id']
#print(watson_collection)
def delete(doc_id):
		delete_doc = discovery.delete_document(watson_environment_id, watson_collection, doc_id)
		print(json.dumps(delete_doc, indent=2))
def config():
	print(discovery.list_configurations(environment_id=watson_environment_id))
	default_config_id = discovery.get_default_configuration_id(environment_id=watson_environment_id)
	print(json.dumps(default_config_id, indent=2))

	default_config = discovery.get_configuration(environment_id=watson_environment_id, configuration_id=default_config_id)
	print(json.dumps(default_config, indent=2))

	with open(os.path.join(os.getcwd(), 'config.json')) as config_data:
	  data = json.load(config_data)
	  new_config = discovery.create_configuration('watson_environment_id', data)
	print(json.dumps(new_config, indent=2))

def add_doc(doc_loc, doc_name):
	with open(os.path.join(os.getcwd(), doc_loc, doc_name), encoding='ISO-8859-1') as fileinfo:
	  add_doc = discovery.add_document(watson_environment_id, watson_collection, file_info=fileinfo)
	print(json.dumps(add_doc, indent=2))

'''
def lookup():
	qopts = {'query': '{query_string}', 'filter': 'enriched_text.entities.text:"A. J. Raffles").term(enriched_text.sentiment.document.label,count:3)', ...}
	my_query = discovery.query(watson_environment_id, watson_collection, qopts)
	print(json.dumps(my_query, indent=2))
'''

count = 4
string_look = '1234 drury lane'
texts = []
textblobs = []
output_text = ''
def natural_language_lookup(s, count):
	qopts = {'natural_language_query': s, 'count': count, 'passages': True}
	my_query = discovery.query(watson_environment_id, watson_collection, qopts)
	#print(json.dumps(my_query, indent=2))
	for x in my_query['passages']:

		texts.append(x['passage_text'])
		textblobs.append(TextBlob(x['passage_text']))

	output = '\n'.join([str("score: "+str(x['passage_score'])+"\ntext: "+x['passage_text']+"\n\n") for x in my_query['passages']])
	for text in textblobs:
		for sentence in text.sentences:
			output_text.join('\n' + str(sentence))
	#easygui.msgbox(str(output_text), 'Watson Says')
	return output, my_query

def print_to_html(output):
	if (len(output) > 30):
		html = '<html>' + output.replace('\n','<br>') + '</html>'
		path = os.path.abspath('temp.html')
		with open(path, 'w') as f:
			f.write(html)
	else:
		path = os.path.abspath(output)
	webbrowser.open('file://'+path)

def process_who_query(output):
	print('y')

	#def Mbox(title, text, style):
	#    return ctypes.cdll.user32.MessageBoxW(0, text, title, style)
	#Mbox('Watson', output, 1)


def backup():
	os.system('clear')
	print("\nWhat can I help you with, mate?\n\n")
	text_question = input()
	while(text_question != 'thanks'):
		question_blob = TextBlob(text_question)
		print('\n\n')
		time.sleep(1)
		if(question_blob.words.count('who')):
			if(question_blob.words.count('killed')>0 or question_blob.words.count('murdered')>0 or question_blob.words.count('did')>0):
				print("I believe it's you're job to find that out, mate.")
			else:
				print('It looks to be Bob Ross, mate.')
		elif(question_blob.words.count('show')):
			print('Here you go, mate.')
			print_to_html('shortstories/report_test_1.pdf')
		else:
			print(response_for_not_knowing[random.randint(0, len(response_for_not_knowing))])

		print('\n\n')
		text_question = input()






question = ''
if len(sys.argv) > 1 and sys.argv[1] !=' t':

	for x in range(1, len(sys.argv)):
		question+=str(sys.argv[x])+' '

	question_blob = TextBlob(question)
	print(str(question_blob.tokens))

	output, query = natural_language_lookup(question, count)
	if (question_blob.words.count('who') > 0 ):
		out_blob = TextBlob(output)
		print(out_blob.tags)
	#print_to_html(output)


#output = natural_language_lookup(string_look, count)
#add_doc('', 'report_test_1.pdf')

#print_to_html(output)

if(str(sys.argv[1]) == 't'):
	backup()

















