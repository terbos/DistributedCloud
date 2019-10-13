# saved as client.py
#import Pyro4

#uri=raw_input("What is the Pyro uri of the greeting object? ").strip()
#name=raw_input("What is your name? ").strip()

#greeting_maker=Pyro4.Proxy(uri)          # get a Pyro proxy to the greeting #object
#print greeting_maker.get_message(name)   # call method normally

# save this as client.py
import Pyro4

class GreetingMaker(object):
    def get_fortune(self, name):
        return "Hello, {0}".format(name)

greeting_maker=GreetingMaker()

daemon=Pyro4.Daemon()                 # make a Pyro daemon
uri=daemon.register(greeting_maker)   # register the greeting object as a Pyro object

print "Ready. Object uri =", uri      # print the uri so we can use it in the client later
daemon.requestLoop()                  # start the event loop of the server to wait for calls
