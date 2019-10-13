import foursquare
from flask import Flask
from flask import jsonify
from flask import request
import os

app = Flask(__name__)

@app.route('/<name>/<lon>,<lat>')
def fourSq(name, lon, lat):
	client = foursquare.Foursquare(client_id='S1XT0F1DYQQCUSWQOZEUX1Y1PHO13MVTUUOZBB1SJASO0AZK', 		client_secret='HMQBGFRPGWZMY2LLZ1BEDBT4WCWKZYFF323MQQPFLJZ4RPTL')
	where = lon+","+lat
	return jsonify(message=client.venues.search(params={'query': name, 'll': where}))

