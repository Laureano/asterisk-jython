from java.io import IOException

from org.asteriskjava.manager import AuthenticationFailedException
from org.asteriskjava.manager import ManagerConnection
from org.asteriskjava.manager import ManagerConnectionFactory
from org.asteriskjava.manager import ManagerEventListener
from org.asteriskjava.manager import TimeoutException
from org.asteriskjava.manager.action import StatusAction
from org.asteriskjava.manager.event import ManagerEvent

import time

class HelloEvents(ManagerEventListener):
    def __init__(self):
        factory = ManagerConnectionFactory("localhost", "manager", "pa55word")
        self.managerConnection = factory.createManagerConnection()

    def run(self):
        # Register for events
        self.managerConnection.addEventListener(self)

        # Connect to Asterisk and log in
        self.managerConnection.login()

        # Request channel state
        self.managerConnection.sendAction(StatusAction())

        # Wait 10 seconds for events to come in
        time.sleep(10)

        # And finally log off and disconnect
        self.managerConnection.logoff()

    def onManagerEvent(self, event):
        # Just print the received events
        print(event)

if __name__ == "__main__":
    helloEvents = HelloEvents()
    helloEvents.run()