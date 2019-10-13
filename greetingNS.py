# saved as greetingNS.py
import Pyro4

class GreetingMaker(object):
    def get_message(self, name):
        return "Hello, {0}".format(name)

greeting_maker=GreetingMaker()

daemon=Pyro4.Daemon()                 # make a Pyro daemon
ns=Pyro4.locateNS()                   # find the name server
uri=daemon.register(greeting_maker)   # register the greeting object as a Pyro object
ns.register("CloudComputing", uri)  # register the object with a name in the name server

print "Ready."
daemon.requestLoop()                  # start the event loop of the server to wait for calls
