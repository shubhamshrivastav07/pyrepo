

from Sub2 import MessageService

class UserChat(MessageService):

    def sendMessage(self):
        print("send message")



u= UserChat()
u.sendMessage()
u.MessageBroker()
u.configurtion()