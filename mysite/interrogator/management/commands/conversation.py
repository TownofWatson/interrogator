from watson_developer_cloud import ConversationV1
import json

conversation = ConversationV1(
	username = 'a2f2135d-5741-4364-803b-66b8116a9b5f',
	password = 'ldTcfTljOKKr',
	version = '2017-05-26'
)

#response = conversation.list_workspaces()
#workspace_id = 'c76dde4b-deb6-4e10-87df-08778b85ce53'

workspace_id = '225a20b1-c3c2-429b-87ba-b389eefc8853'

context = {}
user_input = ''

while True:

	response = conversation.message(
	    workspace_id=workspace_id,
	    input={'text': user_input},
	    context = context
	)

	context = response['context']

	print(json.dumps(response['output']['text'][0],indent=2,ensure_ascii=0))

	user_input = input('>> ')

#if __name__ = "__main__":
#	main()
