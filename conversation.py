from watson_developer_cloud import ConversationV1
import json

conversation = ConversationV1(
	username = 'a2f2135d-5741-4364-803b-66b8116a9b5f',
	password = 'ldTcfTljOKKr',
	version = '2017-05-26'
)

#response = conversation.list_workspaces()
workspaceID = 'c76dde4b-deb6-4e10-87df-08778b85ce53'

response = conversation.message(
    workspace_id=workspaceID,
    input={
        'text': 'start'
    }
)

print(json.dumps(response,indent=2))