# Python HTTP exercises

## Exercise #0: Test HTTP server

Launch the [example Python HTTP server](../../../examples/python/http/server.py) and test it by making a request to it both from a browser and using curl.


## Solution:

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


## Exercise #1: POST requests

Extend the HTTP server to be able to handle POST requests.
Test it by making a post request using curl.
* You can use [this example](https://blog.anvileight.com/posts/simple-python-http-server/#do-get)




## Exercise #2: Form handling

Use the server provided [here](exercise2.py).
Make a HTML form with some input fields and set its action such that it is submitted to your Python HTTP server (using GET). 

  - See [urllib.parse](https://docs.python.org/3/library/urllib.parse.html) for extracting input variables from the URL


## Exercise #3: Form handling (POST)

Extend the previous exercise such that the form is submitted using POST.
