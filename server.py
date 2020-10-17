import cherrypy
import chatterbot
from chatterbot.conversation import Statement as St
import speech_recognition as sr

class TalkingKai:
    def __init__(self):
        self.chatbot = chatterbot.ChatBot("TalkingKai", read_only=True)
        self.recognizer = sr.Recognizer()
    

    def get_chatbot_response(text):
        return self.chatbot.get_response(St(text)).text

    @cherrypy.expose
    def index(self):
        # payload should be 16 bit signed pcm(integer) with rate=16khz
        pcm = bytes()
        while True:
            data = cherrypy.request.body.read(2**16)
            if data:
                pcm += data
            else:
                break
        audiodata = sr.AudioData(pcm, 16000, 2)
        text = self.recognizer.recognize_google(audiodata)
        return self.get_chatbot_response(text)
        

cherrypy.quickstart(TalkingKai())
