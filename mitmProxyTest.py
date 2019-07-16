"""
This example shows two ways to redirect flows to another server.
"""
from mitmproxy import http
from urllib import parse


def request(flow):
	print(flow.request.url)
	if "https://old.reddit.com/api/vote" in flow.request.url:
		newUrl = parse.urlsplit(flow.request.url).query
		#a = dict(parse.parse_qsl(parse.urlsplit(flow.request.url).query))
		#print(a)
		flow.request.url = "http://127.0.0.1:5000/?" + newUrl
	"""if flow.request.pretty_host == "https://oauth.reddit.com/api/vote":
					print(flow.request.path)
					print(flow.request.url)
					flow.request.port = 5000
					#flow.request.host = "127.0.0.1/"
					flow.request.host = "127.0.0.1"
					flow.request.scheme = "http"
					"""
#https://old.reddit.com/api/vote?dir=0&id=t3_a64yhl&sr=hardwareswap
