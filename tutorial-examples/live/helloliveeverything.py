from org.asteriskjava.live import AsteriskChannel
from org.asteriskjava.live import AsteriskQueue
from org.asteriskjava.live import AsteriskServer
from org.asteriskjava.live import AsteriskServerListener
from org.asteriskjava.live import DefaultAsteriskServer
from org.asteriskjava.live import ManagerCommunicationException
from org.asteriskjava.live import MeetMeRoom
from org.asteriskjava.live import MeetMeUser

from java.beans import PropertyChangeListener
from java.beans import PropertyChangeEvent

class HelloLiveEverything(AsteriskServerListener, PropertyChangeListener):
    def __init__(self):
        self.asteriskServer = DefaultAsteriskServer("localhost", "manager", "pa55word")

    def run(self):
        # Listen for new events
        self.asteriskServer.addAsteriskServerListener(self)

        # Add property change listeners to existing objects
        for asteriskChannel in self.asteriskServer.getChannels():
            print(asteriskChannel)
            asteriskChannel.addPropertyChangeListener(self)

        for asteriskQueue in self.asteriskServer.getQueues():
            print(asteriskQueue)
            for asteriskChannel in asteriskQueue.getEntries():
                asteriskChannel.addPropertyChangeListener(self)

        for meetMeRoom in self.asteriskServer.getMeetMeRooms():
            print(meetMeRoom)
            for user in meetMeRoom.getUsers():
                user.addPropertyChangeListener(self)

    def onNewAsteriskChannel(self, channel):
        print(channel)
        channel.addPropertyChangeListener(self)

    def onNewMeetMeUser(self, user):
        print(user)
        user.addPropertyChangeListener(self)

    def propertyChange(self, propertyChangeEvent):
        print(propertyChangeEvent)

if __name__ == "__main__":
    helloLiveEverything = HelloLiveEverything()
    helloLiveEverything.run()