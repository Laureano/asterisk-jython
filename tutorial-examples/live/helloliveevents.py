from org.asteriskjava.live import AsteriskChannel
from org.asteriskjava.live import AsteriskServer
from org.asteriskjava.live import AsteriskServerListener
from org.asteriskjava.live import DefaultAsteriskServer
from org.asteriskjava.live import ManagerCommunicationException
from org.asteriskjava.live import MeetMeUser

import time

class HelloLiveEvents(AsteriskServerListener):
    def __init__(self):
        self.asteriskServer = DefaultAsteriskServer("localhost", "manager", "pa55word")

    def run(self):
        self.asteriskServer.addAsteriskServerListener(self)

    def onNewAsteriskChannel(self, channel):
        print(channel)

    def onNewMeetMeUser(self, user):
        print(user)

if __name__ == "__main__":
    helloLiveEvents = HelloLiveEvents()
    helloLiveEvents.run()