import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
import webbrowser
import DefaultSettings
import json

# TO DO:
# Delete default client id and client secret in get_access_code()
# PCKE

DEFAULT_OAUTH_URL = DefaultSettings.DEFAULT_OAUTH_URL
DEFAULT_REDIRECT_URI = DefaultSettings.DEFAULT_REDIRECT_URI
DEFAULT_CLIENT_ID = DefaultSettings.DEFAULT_CLIENT_ID
DEFAULT_CLIENT_SECRET = DefaultSettings.DEFAULT_CLIENT_SECRET
DEFAULT_API_URL = DefaultSettings.DEFAULT_API_URL


# Implementing function to authorize app and obtain access_code
def get_access_code(client_id=DEFAULT_CLIENT_ID, client_secret=DEFAULT_CLIENT_SECRET, redirect_uri=DEFAULT_REDIRECT_URI,
                    oauth_url=DEFAULT_OAUTH_URL):
    # default class loader
    auth_url = '{}/authorize' \
               '?response_type=code' \
               '&client_id={}' \
               '&client_secret={}' \
               '&redirect_uri={}'.format(oauth_url, client_id, client_secret, redirect_uri)

    # parsing to separate hostname and port
    parsed_redirect_uri = requests.utils.urlparse(redirect_uri)
    server_address = parsed_redirect_uri.hostname, parsed_redirect_uri.port

    # class extending BaseHttpRequestHandler, will help us handle GET request
    class AllegroHTTPAuthHandler(BaseHTTPRequestHandler):
        def __init__(self, request, address, server):
            super().__init__(request, address, server)

        def do_GET(self):
            # Sends a response header, logs the accepted request
            self.send_response(200, "ok")
            # writes header to the output stream
            # (header keyword, header value)
            self.send_header("Content-Type", "text/html")
            # sends a blank line indicating the end of the HTTP headers in response, also invokes flush_headers()
            # which flushes the internal headers buffer
            self.end_headers()
            # path contains the request path
            self.server.access_code = self.path.rsplit("?code=", 1)[-1]

    print("server_address: ", server_address)
    # giving access to app
    webbrowser.open(auth_url)
    # starting httpserver on localhost address
    httpd = HTTPServer(server_address, AllegroHTTPAuthHandler)
    print('Waiting for response with access_code from Allegro.pl (user authorization in progress)...')
    # handle one request
    httpd.handle_request()

    httpd.server_close()

    _access_code = httpd.access_code

    print("Got an authorize code: ", _access_code)

    return _access_code


# default class loader
def sign_in(client_id, client_secret, access_code, redirect_uri='http://localhost:8000', oauth_url=DEFAULT_OAUTH_URL):
    token_url = oauth_url + "/token"

    access_token_data = {'grant_type': "authorization_code",
                         "code": access_code,
                         'redirect_uri': redirect_uri}

    response = requests.post(url=token_url,
                             auth=requests.auth.HTTPBasicAuth(client_id, client_secret),
                             data=access_token_data)
    return response.json()


def get_access_token():
    access_code = get_access_code()
    token = sign_in(DEFAULT_CLIENT_ID, DEFAULT_CLIENT_SECRET, access_code)
    access_token = token["access_token"]
    return access_token




