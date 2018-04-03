import sys
import os
import json
import time
import webbrowser
import mimetypes
#import easygui
#import nltk
#from textblob import TextBlob
#from textblob import Word
from watson_developer_cloud import DiscoveryV1
import random
import ctypes 

response_for_not_knowing = ["Couldn't tell ya, mate", "I'm not quite sure I can answer that.", 
"Well pickle me tender, I've no clue.", "That is a really good question", "Huh",  "You know, there are some questions that even I can't answer",
"My literature doesn't really speak of that"]


	#print(watson_collection)
def delete(doc_id):
		delete_doc = discovery.delete_document(watson_environment_id, watson_collection, doc_id)
		print(json.dumps(delete_doc, indent=2))
		return "deleted"
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
	return "added"

'''
def lookup():
	qopts = {'query': '{query_string}', 'filter': 'enriched_text.entities.text:"A. J. Raffles").term(enriched_text.sentiment.document.label,count:3)', ...}
	my_query = discovery.query(watson_environment_id, watson_collection, qopts)
	print(json.dumps(my_query, indent=2))
'''

def natural_language_lookup(s, count, discovery, watson_environment_id, watson_collection):
	qopts = {'natural_language_query': s, 'count': count, 'passages': True, 'return': ['extracted_metadata.filename']}
	my_query = discovery.query(watson_environment_id, watson_collection, qopts)
	#print(json.dumps(my_query, indent=2))
	#for x in my_query['passages']:

	#	texts.append(x['passage_text'])
	#	textblobs.append(TextBlob(x['passage_text']))

	#print(my_query)
	output = "response"#'\n'.join([str("score: "+str(x['passage_score'])+"\ntext: "+x['passage_text']+"\n\n") for x in my_query['passages']])
	extrac = [str(x['extracted_metadata']['filename']) for x in my_query['results']]
	#docid = '\n'.join([str("score: "+str(x['passage_score'])+"\ntext: "+x['passage_text']+"\n\n") for x in my_query['passages']])

	# for text in textblobs:
	# 	for sentence in text.sentences:
	# 		output_text.join('\n' + str(sentence))
	#easygui.msgbox(str(output_text), 'Watson Says')
	return output, my_query, extrac


# def pdf_view(request):
# 	path = os.path.abspath(request)
#     with open(path, 'r') as pdf:
#         response = HttpResponse(pdf.read(), mimetype='application/pdf')
#         response['Content-Disposition'] = 'inline;filename=some_file.pdf'
#         return response
#     pdf.closed


def print_to_html(output):
	if (len(output) > 50):
		html = '<html>' + output.replace('\n','<br>') + '</html>'
		path = os.path.abspath('temp.html')
		#print(path)
		with open(path, 'w') as f:
			f.write(html)
	else:
		path = os.path.abspath(output)
		print(path)

	webbrowser.open('file://'+path)
	return True





def process_who_query(output):
	return True

	#def Mbox(title, text, style):
	#    return ctypes.cdll.user32.MessageBoxW(0, text, title, style)
	#Mbox('Watson', output, 1)


def backup():
	os.system('clear')
	print("\nWhat can I help you with, mate?\n\n")
	# text_question = input()
	# while(text_question != 'thanks'):
	# 	question_blob = TextBlob(text_question)
	# 	print('\n\n')
	# 	time.sleep(3)
	# 	if(question_blob.words.count('who')):
	# 		if(question_blob.words.count('killed')>0 or question_blob.words.count('murdered')>0 or question_blob.words.count('did')>0):
	# 			print("I believe it's your job to find that out, mate.")
	# 		elif(question_blob.words.count('Knife')):
	# 			print("A knife was found with Bob Ross's fingerprints, and various acrylic paints, mate.")
	# 		else:
	# 			print('It looks to be Bob Ross, mate.')
	# 	elif(question_blob.words.count('show')):
	# 		print('Here you go, mate.')
	# 		print_to_html('shortstories/report_test_1.pdf')
	# 	else:
	# 		print(response_for_not_knowing[random.randint(0, len(response_for_not_knowing))])

	# 	print('\n\n')
	# 	text_question = input()


def watson_opinion(question_blob, extrac):
	name = "default"
	# if(question_blob.words.count('show')):
	# 	print(extrac)
	# 	print_to_html('pdfs/gen/'+str(extrac[0]))
	# elif(question_blob.words.count('who')):
	# 	if(question_blob.words.count('killed')>0 or question_blob.words.count('murdered')>0 or question_blob.words.count('did')>0):
	# 		print("I believe it's your job to find that out, mate.")
	# 	elif(question_blob.words.count('Knife')):
	# 		print("A knife was found with " + name + "'s fingerprints")
	# 	else:
	# 		print('It looks to be '+name+', mate.')
	# else:
	# 		print(response_for_not_knowing[random.randint(0, len(response_for_not_knowing))])



def connect():
	discovery = DiscoveryV1(
		username="adbf14e6-bc4b-4f02-a71f-e3914e61f623",
		password="OlSYr70ryMdK",
		version="2017-11-07"
	)
	print(discovery)
	#environments = discovery.list_environments()
	environments = discovery.get_environments()

	#print(environments)
		#print(json.dumps(environments, indent=2))

	watson_environments = [x for x in environments['environments'] if x['name'] == 'my_environment']
	#print(watson_environments)
	watson_environment_id = watson_environments[0]['environment_id']
		#print(json.dumps(watson_environment_id, indent=2))

	collections = discovery.list_collections(watson_environment_id)
	watson_collections = [x for x in collections['collections']]

	for x in watson_collections:
		if(x['name'] == 'crimereports'):
			watson_collection = x['collection_id']

	return discovery, environments, watson_environments, watson_environment_id, collections, watson_collections, watson_collection


def main_run(question):
	discovery, environments, watson_environments, watson_environment_id, collections, watson_collections, watson_collection = connect()

	question_blob = '-' #TextBlob(question)
	#print(str(question_blob.tokens))

	output, query, extrac = natural_language_lookup(question, count, discovery, watson_environment_id, watson_collection)
	name = "default"
	response = 999999999
	if(len(extrac) > 0):
		print("I've found some relevant documents for ya \n")
		while(response != (len(extrac)+1)):
			list_options(extrac)

			response = input()

			while(len(response) != 1):
				print("I only understand numbers, beep boop")
				response = input()

			response = int(response)

			handle_list_response(response, extrac, question_blob)

	else:
		print("I've got nothin for ya")


def ask_watson(question):
	discovery, environments, watson_environments, watson_environment_id, collections, watson_collections, watson_collection = connect()

	question_blob = '-' #TextBlob(question)
	#print(str(question_blob.tokens))
	respond = ''
	output, query, extrac = natural_language_lookup(question, count, discovery, watson_environment_id, watson_collection)
	name = "default"
	response = 999999999
	if(len(extrac) > 0):
		#creating response

		respond = respond + "I've found some relevant documents for ya"

		#respond = respond + list_options_res(extrac)

	else:
		respond = respond + "I've got nothin for ya"
	return respond, extrac


def ask_watson_response(response, extrac):
	if(len(response)!= 1):
		return 0,"I only understand numbers, beep boop"
	else:
		response = int(response)
		return 1, handle_list_response_ask(response, extrac)


def list_options_res(extrac):
	respond = ''
	for file_num in range(0, len(extrac)):
		respond = respond + str(file_num) + ". " + extrac[file_num] + "\n"

	respond = respond + str(len(extrac)) + " None of these\n"
	respond = respond + str(len(extrac)+1) + " Done.\n"
	return respond
	#print("\n" + str(len(extrac)+1) + " Or do you want me to look through them and give my opinion?")


def list_options(extrac):

	for file_num in range(0, len(extrac)):
		print(str(file_num) + ". " + extrac[file_num])

	print(str(len(extrac)) + " None of these")
	print(str(len(extrac)+1) + " Done.")
	#print("\n" + str(len(extrac)+1) + " Or do you want me to look through them and give my opinion?")

def handle_list_response_ask(response, extrac):
	text_response = "Hmm\n\n"
	if((response) == len(extrac)+1):
		text_response = "Hope I helped."
		#watson_opinion(question_blob, extrac)

	elif((response) == len(extrac)):

		text_response = "Sorry mate, I just can't find anything relevant"

	elif(response > len(extrac)):

		text_response = "OOB\n\n"

	else:
		text_response = "Here ya go mate"
		print_to_html('pdfs/gen/'+str(extrac[response]))
		#pdf_to_html('pdfs/gen/'+str(extrac[response]))

	return(text_response)

def handle_list_response(response, extrac, question_blob):
	text_response = "Hmm\n\n"
	if((response) == len(extrac)+1):
		text_response = "Hope I helped.\n\n"
		#watson_opinion(question_blob, extrac)

	elif((response) == len(extrac)):

		text_response = "Sorry mate, I just can't find anything relevant\n\n"

	elif(response > len(extrac)):

		text_response = "OOB\n\n"

	else:
		text_response = "Here ya go mate\n\n"
		print_to_html('pdfs/gen/'+str(extrac[response]))
		#pdf_to_html('pdfs/gen/'+str(extrac[response]))

	print(text_response)

	#print_to_html(output)


#output = natural_language_lookup(string_look, count)
#add_doc('', 'report_test_1.pdf')

#print_to_html(output)
count = 4
string_look = '1234 drury lane'
texts = []
textblobs = []
output_text = ''
question = ''

if(len(sys.argv) > 1) and (str(sys.argv[1]) == 't'):

	backup()
	
elif(len(sys.argv) > 1):

	for x in range(1, len(sys.argv)):
		question+=str(sys.argv[x])+' '

if(len(question) > 1):
	main_run(question)














