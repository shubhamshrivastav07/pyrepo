

from Sub2 import MessageService

class Notifications(MessageService):

    def sendNotify(self):
        print("Notification Send")



n= Notifications()
n.configurtion()
n.MessageBroker()
n.sendNotify()