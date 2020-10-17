import cherrypy
import chatterbot
from chatterbot.conversation import Statement as St
import os

class TalkingKai:
    def __init__(self):
        self.chatbot = chatterbot.ChatBot("TalkingKai", read_only=True)

    def get_chatbot_response(self, text):
        return self.chatbot.get_response(St(text)).text

    @cherrypy.expose
    def index(self, text=""):
        if text=="":
            return "" 
        return self.get_chatbot_response(text)
        
conf= {"global": {
    "server.socket_host": "0.0.0.0",
    "server.socket_port": int(os.getenv("PORT"))
    }}
cherrypy.quickstart(TalkingKai(), "/", conf)
