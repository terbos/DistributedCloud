# saved as clientNS.py
import Pyro4

name=raw_input("What is your name? ").strip()

greeting_maker=Pyro4.Proxy("CloudComputing")    # use name server object lookup uri shortcut
print greeting_maker.get_message(name)
