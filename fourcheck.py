import httplib
from flask import request
from flask import Flask
from flask import jsonify


conn = httplib.HTTPConnection("prop-four-square.herokuapp.com")


what = raw_input('What do we want? ').strip()
longitude = raw_input('Longitude? ').strip()
latitude = raw_input('Latitude? ').strip()

search = "/"+what+"/"+longitude+","+latitude

conn.request("GET", search)

r1 = conn.getresponse()

print (r1.status, r1.reason, r1.read())

conn.close()
