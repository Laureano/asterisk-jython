from org.asteriskjava.live import AsteriskServer
from org.asteriskjava.live import AsteriskChannel
from org.asteriskjava.live import AsteriskQueue
from org.asteriskjava.live import MeetMeRoom
from org.asteriskjava.live import DefaultAsteriskServer

from org.asteriskjava.live import ManagerCommunicationException

import time

class HelloLive:
    def __init__(self):
        self.asteriskServer = DefaultAsteriskServer("localhost", "manager", "pa55word")

    def run(self):
        for asteriskChannel in self.asteriskServer.getChannels():
            print(asteriskChannel)
        for asteriskQueue in self.asteriskServer.getQueues():
            print(asteriskQueue)
        for meetMeRoom in self.asteriskServer.getMeetMeRooms():
            print(meetMeRoom)

if __name__ == "__main__":
    helloLive = HelloLive()
    helloLive.run()