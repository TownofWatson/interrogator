import sys
import os
import json
import webbrowser
import mimetypes
import easygui
from watson_developer_cloud import DiscoveryV1
import ctypes  

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
def natural_language_lookup(s, count):
	qopts = {'natural_language_query': s, 'count': count, 'passages': True}
	my_query = discovery.query(watson_environment_id, watson_collection, qopts)
	#print(json.dumps(my_query, indent=2))

	output = '\n'.join([str("score: "+str(x['passage_score'])+"\ntext: "+x['passage_text']+"\n\n") for x in my_query['passages']])
	print(output)
	#easygui.msgbox(str(my_query), 'Watson Says')

	return output + str(my_query)

def print_to_html(output):
	html = '<html>' + output.replace('\n','<br>') + '</html>'
	path = os.path.abspath('temp.html')
	with open(path, 'w') as f:
		f.write(html)
	webbrowser.open('file://'+path)


	def Mbox(title, text, style):
	    return ctypes.cdll.user32.MessageBoxW(0, text, title, style)
	Mbox('Watson', output, 1)


output = natural_language_lookup(string_look, count)
#add_doc('', 'report_test_1.pdf')

print_to_html(output)



















