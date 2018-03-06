from watson_developer_cloud import ConversationV1
import json
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as scrolledtext
import tkinter.font as font

conversation = ConversationV1(
	username = 'a2f2135d-5741-4364-803b-66b8116a9b5f',
	password = 'ldTcfTljOKKr',
	version = '2017-05-26'
)

#response = conversation.list_workspaces()
workspace_id = 'c76dde4b-deb6-4e10-87df-08778b85ce53'

class InterrogateWindow(tk.Tk):

	def __init__(self):
		tk.Tk.__init__(self)
		self.textFont = font.Font(family="Helvetica",size=30)

		self.title("Interrogate")		
		self.initialize()

	def initialize(self):
		self.context = {}
		self.grid()
		self.columnconfigure(0,weight=1)
		self.rowconfigure(0,weight=1)

		self.respond = ttk.Button(self, text='Respond', command=self.get_response)
		self.respond.grid(column=1, row=1, sticky='nesw', padx=3, pady=3)

		self.usr_input = ttk.Entry(self, state='normal')
		self.usr_input.bind("<Return>",(lambda event: self.get_response()))
		self.usr_input.grid(column=0, row=1, sticky='nesw', padx=3, pady=3)

		self.conversation = scrolledtext.ScrolledText(self, state='disabled',font=self.textFont,wrap='word')
		self.conversation.grid(column=0, row=0, columnspan=2, sticky='nesw', padx=3, pady=3)

		self.start_session()

	def start_session(self):
		user_input = ''
		response = conversation.message(
			workspace_id=workspace_id,
			message_input={'text': user_input},
			context = self.context,	
		)
		self.context = response['context']
		self.conversation['state'] = 'normal'
		self.conversation.insert(tk.END, json.dumps(response['output']['text'][0],indent=2) + "\n\n")
		self.conversation['state'] = 'disabled'


	def get_response(self):
		user_input = self.usr_input.get()
		self.usr_input.delete(0, tk.END)

		response = conversation.message(
			workspace_id=workspace_id,
			message_input={'text': user_input},
			context = self.context
		)

		self.context = response['context']

		self.conversation['state'] = 'normal'
		self.conversation.insert(tk.END, "User: " + user_input + "\n" + json.dumps(response['output']['text'][0],indent=2) + "\n\n")
		self.conversation.see(tk.END)
		self.conversation['state'] = 'disabled'



start = InterrogateWindow()
start.mainloop()


'''
root = Tk()
root.title("Interrogator")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))


ttk.Button(mainframe, text="Start").grid(column=3, row=3, sticky=W)

root.mainloop()


# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Interrogator")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        #chat = Text(self, width=58, height=15)
        #chat.place(x=0,y=0)

        self.user_input = StringVar()

        text = Entry(self, width=48,textvariable=self.user_input)

        text.place(x=5,y=225)

        # creating a button instance
        sendButton = Button(self, text="Send",command=self.send)

        # placing the button on my window
        sendButton.place(x=180, y=250)

       

    def send(self):
        label = Label(self,textvariable=self.user_input)
        label.place(x=0,y=0)

# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("400x300")

#creation of an instance
app = Window(root)

#mainloop 
root.mainloop()
'''
'''
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
'''
#if __name__ = "__main__":
#	main()
