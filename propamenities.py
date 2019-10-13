import Pyro4
import httplib
from flask import request
from flask import Flask

import json


housenum=raw_input("How number: ").strip()
propID=raw_input("Enter the Postcode: ").strip()
amenity=raw_input("What are you searching for: ").strip()

push_property=Pyro4.Proxy("PYRONAME:property.id")

a = push_property.scanProplist(propID) 

conn = httplib.HTTPConnection("prop-four-square.herokuapp.com")

search = "/"+amenity+"/"+a[0]+","+a[1]

conn.request("GET", search)

r1 = conn.getresponse()


results = json.loads(r1.read())
#Not me.


for venue in results['message']['venues']:
	print venue['name']
	print "Distance from Postcode: ",venue['location']['distance'], "meters"
	print


conn.close()
