from concussion import Application, Service
from concussion.protocols import http

def hello_http(req):
	content = "Hello, Worldz!"
	headers = http.HttpHeaders()
	headers.add('Content-Length', len(content))
	headers.add('Content-Type', 'text/plain')
	return http.http_response(req, 200, headers, content)

app = Application()
app.add_service(Service(http.HttpServer(hello_http), 8015))
app.run()