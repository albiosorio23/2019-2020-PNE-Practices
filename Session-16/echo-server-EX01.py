import http.server
import socketserver
import termcolor
from pathlib import Path

# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Analize the request line
        req_line = self.requestline.split(' ')

        # Get the path. It always start with the / symbol
        path = req_line[1]

        # separamos el path,  lo que está antes del ? y lo que está depues
        arguments = path.split("?")

        action_echo = arguments[0]

        if action_echo == "/": # Manda la pg principal
            contents = Path("form-1.html").read_text()
            status = 200

        elif action_echo == "/echo": #Escribe en la pg principal
            # después del ?
            input = arguments[1]
            # Separar el mensaje de lo que escribe el cliente
            input_name = input.split("=")[0]
            input_value = input.split("=")[1]
            contents = Path("form-EX01.html").read_text()
            #Para añadir el mensaje del cliente
            contents = contents + f"<p>{input_value}</p>"
            status = 200

        else:
            # -- Resource NOT FOUND
            termcolor.cprint("ERROR: Not found", 'red')

            # Message to send back to the clinet
            contents = Path("Error.html").read_text()

            # Status code is NOT FOUND
            status = 404


        # Generating the response message
        self.send_response(status)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()