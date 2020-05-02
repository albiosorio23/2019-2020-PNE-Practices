import http.server
import socketserver
import termcolor
from pathlib import Path
import json
from Seq1 import Seq

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

Server = "rest.ensembl.org"
Parameters ="?content-type=application/json"

# Connect with the server
conn = http.client.HTTPConnection(Server)



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

        endpoint = arguments[0]

        if endpoint == "/":  # Manda la pg principal
            contents = Path("Finalproject.html").read_text()
            status = 200

        #elif endpoint == "/listSpecies":  # Escribe en la pg principal
            # después del ?
            #limit_and_number = arguments[1]
            #number = limit_and_number.split("=")[1]
            #status = 200

        elif endpoint == "/listSpecies":
            # Coger lo que está despues del interrogante (limit=10)
            limit_number = arguments[1]
            # Coger la especie que seleccionas
            limit = limit_number.split("=")[1]
            Endpoint = "/info/species"
            #esta es la re line para bucar la información
            Request_line = Endpoint + Parameters

            try:
                conn.request("GET", Request_line)
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()

            # -- Read the response message from the server
            r1 = conn.getresponse()

            # -- Read the response's body
            data1 = r1.read().decode("utf-8")

            # -- Create a variable with the data,
            # -- form the JSON received
            name_specie_ = json.loads(data1)
            name_specie = name_specie_["species"]
            #count = 0
            #list = []
            if limit == "":
                contents = f""" 
                            <!DOCTYPE html>
                            <html lang = "en">
                            <head>
                            <meta charset = "utf-8" >
                              <title> Information about the karyotype </title >
                            </head >
                            <body>
                            <body style="background-color: lightblue;">
                            <h2> Total number of species is: 267</h2>
                            </body>
                            </html>
                            """

                for element in name_specie:
                    contents = contents + f""" <p> {element["common_name"]} </p>"""

            elif int(limit) > 267:
                contents = Path('Error.html').read_text()
                status = 404
            else:
                contents = f""" 
                            <!DOCTYPE html>
                            <html lang = "en">
                            <head>
                            <meta charset = "utf-8" >
                              <title> Information about the karyotype </title >
                            </head >
                            <body>
                            <body style="background-color: lightblue;">
                            <h2> Total number of species is: 267</h2>
                            <p> The limit you have selected is: {limit} </p>
                            <p> The name of the species are: </p>
                            </body>
                            </html>
                            """
                status = 200
                for element in name_specie[:int(limit)]:
                    contents = contents + f""" <p> . {element["common_name"]}</p>"""

        elif endpoint == "/karyotype":
            # Coger lo que está despues del interrogante (specie=mouse)
            specie_name = arguments[1]
            # Coger la especie que seleccionas
            name_specie = specie_name.split("=")[1]
            Endpoint = "/info/assembly/"
            #esta es la re line para bucar la información
            Request_line = Endpoint + name_specie + Parameters

            try:
                conn.request("GET", Request_line)
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()

            # -- Read the response message from the server
            r1 = conn.getresponse()

            # -- Print the status line
            #print(f"Response received!: {r1.status} {r1.reason}\n")

            # -- Read the response's body
            data1 = r1.read().decode("utf-8")

            # -- Create a variable with the data,
            # -- form the JSON received
            k_specie = json.loads(data1)


            # POnemos la f antes para que así te añada las seq y el número seleccionado
            contents = f""" 
                        <!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8" >
                          <title> Information about the karyotype </title >
                        </head >
                        <body>
                        <body style="background-color: lightblue;">
                        <h2> The names of the chromosomes are:</h2>
                        <p> {k_specie["karyotype"]} </p>
                        </body>
                        </html>
                        """
            status = 200

        elif endpoint == "/chromosomeLength":
            # Coger lo que está despues del interrogante (specie=mouse&chromo=18)
            specie_chromo = arguments[1]
            # Coger la especie que seleccionas
            name_specie = specie_chromo.split("&")[0].split("=")[1]
            number_chromo = specie_chromo.split("&")[1].split("=")[1]
            Endpoint = "/info/assembly/"
            # esta es la req line para bucar la información
            Request_line = Endpoint + name_specie + "/" + number_chromo + Parameters

            try:
                conn.request("GET", Request_line)
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()

            # -- Read the response message from the server
            r1 = conn.getresponse()

            # -- Print the status line
            # print(f"Response received!: {r1.status} {r1.reason}\n")

            # -- Read the response's body
            data1 = r1.read().decode("utf-8")

            # -- Create a variable with the data,
            # -- form the JSON received
            l_chromosome = json.loads(data1)

            # POnemos la f antes para que así te añada las seq y el número seleccionado
            contents = f""" 
                        <!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8" >
                            <title> Information about the karyotype </title >
                        </head >
                        <body>
                        <body style="background-color: lightblue;">
                        <h2> The length of the chromosome is: {l_chromosome["length"]}</h2>
                        </body>
                        </html>
                        """
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