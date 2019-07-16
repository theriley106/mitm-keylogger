from mitmproxy import http

def response(flow: http.HTTPFlow) -> None:
    flow.response.content = flow.response.content.replace(b"type=\"password\"", b"type=\"notPassword\"")
