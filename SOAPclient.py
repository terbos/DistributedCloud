from suds.client import Client
from suds.sax.element import Element


hello_client = Client('http://localhost:5007/?wsdl')

clientid = raw_input("Property ID? ").strip()

result=hello_client.service.send_location(clientid)

print hello_client.last_sent()
print hello_client.last_received()
