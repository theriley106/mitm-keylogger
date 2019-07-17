#!/usr/bin/python

from __future__ import print_function
from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session
import urllib
import json
import logging
import sys
from flask_sslify import SSLify

app = Flask(__name__, static_url_path='/static')
log = logging.getLogger('werkzeug')
log.disabled = True

@app.route('/', methods=['GET'])
def index():
	jsonString = str(urllib.unquote(str(request.url))).partition("=")[2]
	jsonString = json.loads(jsonString)
	#print("\n")
	print(''.join([v['k'] for v in sorted(jsonString, key=lambda k: k['t'])]))
	#print request.url
	return "AYY"

@app.route('/test', methods=['GET'])
def testPage():
	return render_template("index1.html")

if __name__ == '__main__':
	app.run(port=8000)
