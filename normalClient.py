# save this as client.py
import normalGreeting
name=raw_input("What is your name? ")
greeting_maker=normalGreeting.GreetingMaker()
print greeting_maker.get_message(name)
