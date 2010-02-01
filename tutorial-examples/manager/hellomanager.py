from java.io import IOException

from org.asteriskjava.manager import AuthenticationFailedException
from org.asteriskjava.manager import ManagerConnection
from org.asteriskjava.manager import ManagerConnectionFactory
from org.asteriskjava.manager import TimeoutException
from org.asteriskjava.manager.action import OriginateAction
from org.asteriskjava.manager.response import ManagerResponse

class HelloManager:
    def __init__(self):
        factory = ManagerConnectionFactory("localhost", "manager", "pa55word")
        self.managerConnection = factory.createManagerConnection()

    def run(self):
        originateAction = OriginateAction()
        originateAction.setChannel("SIP/John")
        originateAction.setContext("default")
        originateAction.setExten("1300")
        originateAction.setPriority(1)
        originateAction.setTimeout(30000)

        # Connect to Asterisk and log in
        self.managerConnection.login()

        # Send the originate action and wait for a maximum of 30 seconds for
        # Asterisk to send a reply
        originateResponse = self.managerConnection.sendAction(originateAction, 30000)

        # Print out wheter the originate succeeded or not
        print(originateResponse.getResponse())

        # And finally log off and disconnect
        self.managerConnection.logoff()

if __name__ == "__main__":
    helloManager = HelloManager()
    helloManager.run()