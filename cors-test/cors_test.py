from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class CORSEnabledHandler(webapp.RequestHandler):
    def get(self):
        add_header = self.response.headers.add_header
        if 'Origin' in self.request.headers:
            add_header("Access-Control-Allow-Origin", self.request.headers['Origin'])
        else:
            add_header("Access-Control-Allow-Origin", '*')

        if 'Access-Control-Request-Headers' in self.request.headers:
            add_header('Access-Control-Allow-Headers', self.request.headers['Access-Control-Request-Headers'])

        if 'Access-Control-Request-Method' in self.request.headers:
            add_header('Access-Control-Allow-Methods', self.request.headers['Access-Control-Request-Method'])

        add_header('Access-Control-Max-Age', '0')

        add_header("Access-Control-Allow-Credentials", "true")

        add_header('Cache-Control', 'no-cache')
        add_header('Expires', 'Fri, 01 Jan 1990 00:00:00 GMT')
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write('{"status":"ok"}')

    post = put = head = options = delete = trace = get

application = webapp.WSGIApplication([('/test', CORSEnabledHandler)], debug=True)

if __name__ == "__main__":
    run_wsgi_app(application)
