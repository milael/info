"""
## Exercise #0: Test HTTP server

Launch the [example Python HTTP server](../../../examples/python/http/server.py) and test 
it by making a request to it both from a browser and using curl.
"""

"""
Simple HTTP server.

https://docs.python.org/3/library/http.server.html
"""

from http.server import BaseHTTPRequestHandler, HTTPServer

class myHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    """
    HTTPRequestHandler class

    Parsing of the request is done by the base class BaseHTTPRequestHandler.
    """

    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = "Hello world!"
        # Write message content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

def main():
    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, myHTTPServer_RequestHandler)
    print("running server...")
    httpd.serve_forever()

if __name__ == "__main__":
    main()


"""
Solution:

Run the server: Save the server code in a Python file (e.g., server.py), and then run it by
executing the file in your Python environment. You should see the message "running server..."
 indicating that the server is running and listening for requests.

Test with a web browser:

- Open a web browser.
- Enter the URL http://127.0.0.1:8080 in the browser's address bar and press Enter.
- The browser will send a GET request to the server, and you should see the response
 "Hello world!" displayed in the browser window.

Test with curl:

- Open a terminal or command prompt.
- Type the following command and press Enter:
       - curl http://127.0.0.1:8080
       OR
       - curl http://localhost:8080

Both methods will send a GET request to the server at http://127.0.0.1:8080, 
and you will receive the "Hello world!" response in the respective client (browser or terminal).
 This confirms that the server is working correctly and responding to requests.

Note: Make sure the server is running while you're testing it with either method, 
as the server needs to be actively listening for requests in order to respond.

"""