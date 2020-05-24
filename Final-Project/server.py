import http.server
import socketserver
import termcolor
from pathlib import Path
import json
from Seq1 import Seq

PORT = 8080
Server = "rest.ensembl.org"
Parameters = "?content-type=application/json"
# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


def server(Request_line):
    # Connect with the server
    conn = http.client.HTTPConnection(Server)
    try:
        conn.request("GET", Request_line)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # Read the response message from the server
    r1 = conn.getresponse()

    # Read the response's body
    data = r1.read().decode("utf-8")
    data1 = json.loads(data)

    return data1


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

        if endpoint == "/":  # Main page
            contents = Path("Finalproject.html").read_text()
            status = 200

#------------------------------------------- BASIC LEVEL ------------------------------------------------

        elif endpoint == "/listSpecies":
            # Get what is after ? (limit=10)
            limit_number = arguments[1]
            # Get selected specie
            limit = limit_number.split("=")[1]
            Endpoint = "/info/species"
            # This is the req line to search the info
            Request_line = Endpoint + Parameters

            # Create a variable with the data, form the JSON received
            name_specie = server(Request_line)["species"]

            count_species = 0
            for element in name_specie:
                count_species = count_species + 1
            contents = f""" 
                        <!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8" >
                          <title> List of species </title >
                        </head >
                        <body>
                        <p> Total number of species is: {count_species} </p>
                        <body style="background-color: lightblue;">
                        </body>
                        </html>
                        """
            if limit == "":
                contents += f"""<a href="/">Main page</a>"""
                status = 200

            elif int(limit) > count_species:
                contents = Path('Error.html').read_text()
                status = 404
            else:
                contents = contents + f""" <p> The limit you have selected is: {limit}</p>
                        <p> The name of the species are: </p>"""

                status = 200
                for element in name_specie[:int(limit)]: # Fron the beginning to the limit introduced by the client
                    contents += f""" <p>   • {element["common_name"]}</p>"""
                contents += f"""<a href="/">Main page</a>"""

        elif endpoint == "/karyotype":
            # Get what is after ? (specie=mouse)
            specie_name = arguments[1]
            # Get selected specie
            name_specie = specie_name.split("=")[1]
            Endpoint = "/info/assembly/"
            # This is the req line to search the info
            Request_line = Endpoint + name_specie + Parameters
            try:
                # Check if the req line is ok
                Request_line.isidentifier()
                # Create a variable with the data,form the JSON received
                k_specie = server(Request_line)
                contents = f""" 
                           <!DOCTYPE html>
                           <html lang = "en">
                           <head>
                           <meta charset = "utf-8" >
                             <title> Information about the karyotype </title >
                           </head >
                           <body>
                           <body style="background-color: lightblue;">
                           <p>The names of the chromosomes are:</p>
                           </body>
                           </html> 
                           """
                status = 200
                for element in k_specie["karyotype"]:
                    contents += f"""<p>{element}</p>"""
                contents += f"""<a href="/">Main page</a>"""

            except KeyError:
                contents = Path("Error.html").read_text()
                status = 404


        elif endpoint == "/chromosomeLength":
            # Get what is after ? (specie=mouse&chromo=18)
            specie_chromo = arguments[1]
            # Get the specie that we select
            name_specie = specie_chromo.split("&")[0].split("=")[1]
            number_chromo = specie_chromo.split("&")[1].split("=")[1]
            Endpoint = "/info/assembly/"
            # This is the req line to search the info
            Request_line = Endpoint + name_specie + "/" + number_chromo + Parameters
            try:
                # Check if the req line is ok
                Request_line.isidentifier()
                # Create a variable with the data, form the JSON received
                l_chromosome = server(Request_line)
                contents = f""" 
                            <!DOCTYPE html>
                            <html lang = "en">
                            <head>
                            <meta charset = "utf-8" >
                                <title> Length of the selected chromosome </title >
                            </head >
                            <body>
                            <body style="background-color: lightblue;">
                            <p> The length of the chromosome is: {l_chromosome["length"]}</p>
                            <a href="/">Main page</a>
                            </body>
                            </html>
                            """
                status = 200

            except KeyError:
                contents = Path("Error.html").read_text()
                status = 404

# ------------------------------------------- MEDIUM LEVEL ------------------------------------------------

        elif endpoint == "/geneSeq":
            gene_name = arguments[1]
            gene = gene_name.split("=")[1]
            Endpoint = "/xrefs/symbol/homo_sapiens/"
            # This is the req line to prove that the gene is en human
            Request_line = Endpoint + gene + Parameters
            try:
                # Check if the req line is ok
                Request_line.isidentifier()
                # Create a variable with the data,form the JSON received
                json_gene = server(Request_line)
                id = json_gene[0]["id"]
                Request_line_1 = "/sequence/id/" + id + Parameters
                json_seq = server(Request_line_1)
                contents = f""" 
                            <!DOCTYPE html>
                            <html lang = "en">
                            <head>
                            <meta charset = "utf-8" >
                                <title> Human gene sequence </title >
                            </head >
                            <body>
                            <body style="background-color: lightpink;">
                            <p> The sequence of the human gene is: {json_seq["seq"]}</p>
                            <a href="/">Main page</a>
                            </body>
                            </html>
                            """
                status = 200

            except IndexError:
                contents = Path("Error.html").read_text()
                status = 404

        elif endpoint == "/geneInfo":
            gene_name = arguments[1]
            gene = gene_name.split("=")[1]
            Endpoint = "/xrefs/symbol/homo_sapiens/"
            # This is the req line to search the info
            Request_line = Endpoint + gene + Parameters
            try:
                # Check if the req line is ok
                Request_line.isidentifier()
                # Create a variable with the data,form the JSON received
                json_gene = server(Request_line)
                id = json_gene[0]["id"]
                Request_line_1 = "/lookup/id/" + id + Parameters
                # Create a variable with the data,form the JSON received
                json_info = server(Request_line_1)
                length = json_info["end"] - json_info["start"]
                contents = f""" 
                            <!DOCTYPE html>
                            <html lang = "en">
                            <head>
                            <meta charset = "utf-8" >
                                <title> Human gene information </title >
                            </head >
                            <body>
                            <body style="background-color: lightpink;">
                            <h> Information about the human gene: </h>
                            <p> Start: {json_info["start"]}</p>
                            <p> End: {json_info["end"]}</p>
                            <p> Length: {length}</p>
                            <p> Id: {json_info["id"]}</p>
                            <p> Chromose: {json_info["seq_region_name"]}</p>
                            <a href="/">Main page</a>
                            </body>
                            </html>
                            """
                status = 200

            except IndexError:
                contents = Path("Error.html").read_text()
                status = 404

        elif endpoint == "/geneCalc":
            gene_name = arguments[1]
            gene = gene_name.split("=")[1]
            Endpoint = "/xrefs/symbol/homo_sapiens/"
            # This is the req line to search the info
            Request_line = Endpoint + gene + Parameters
            try:
                # Check if the req line is ok
                Request_line.isidentifier()
                # Create a variable with the data,form the JSON received
                json_gene = server(Request_line)
                id = json_gene[0]["id"]
                Request_line_1 = "/sequence/id/" + id + Parameters
                json_seq = server(Request_line_1)
                seq_ = json_seq["seq"]
                seq = Seq(seq_)
                seq_length = seq.len()

                number_of_A = seq.count_base("A")
                percentage_A = "{:.1f}".format(100 * number_of_A / seq_length)
                number_of_G = seq.count_base("G")
                percentage_G = "{:.1f}".format(100 * number_of_G / seq_length)
                number_of_T = seq.count_base("T")
                percentage_T = "{:.1f}".format(100 * number_of_T / seq_length)
                number_of_C = seq.count_base("C")
                percentage_C = "{:.1f}".format(100 * number_of_C / seq_length)

                contents = f""" 
                            <!DOCTYPE html>
                            <html lang = "en">
                            <head>
                            <meta charset = "utf-8" >
                                <title> Human gene sequence </title >
                            </head >
                            <body>
                            <body style="background-color: lightpink;">
                            <h>Calculations on the human gene: </h>
                            <p>Total legth: {seq_length}</p>
                            <p>A: {percentage_A}%</p>
                            <p>C: {percentage_C}%</p>
                            <p>G: {percentage_G}%</p>
                            <p>T: {percentage_T}%</p>
                            <a href="/">Main page</a>
                            </body>
                            </html>
                            """
                status = 200

            except IndexError:
                contents = Path("Error.html").read_text()
                status = 404

        elif endpoint == "/geneList":
            chromo_start_end = arguments[1]
            chromo = chromo_start_end.split("&")[0].split("=")[1]
            start = chromo_start_end.split("&")[1].split("=")[1]
            end = chromo_start_end.split("&")[-1].split("=")[1]
            Endpoint = "/overlap/region/human/"
            # This is the req line to search the info
            Request_line = Endpoint + chromo + ":" + start + "-" + end + "?feature=gene;feature=transcript;feature=cds;feature=exon;content-type=application/json"

            try:
                # Check if the req line is ok
                Request_line.isidentifier()
                # Create a variable with the data,form the JSON received
                json_name = server(Request_line)

                contents = f""" 
                        <!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8" >
                            <title> Human gene sequence </title >
                        </head >
                        <body>
                        <body style="background-color: lightpink;">
                        <p> The names of the genes located in the chromosome {chromo} from {start} to {end}:</p>
                        <a href="/">Main page</a>
                        </body>
                        </html>
                        """
                status = 200
                for element in json_name:

                    try:
                        name= element["external_name"]
                        contents += f"""<p>{name}</p>"""
                    except KeyError:
                        contents += f"""<p>{element["id"]}</p>"""


            except KeyError:
                contents = Path("Error.html").read_text()
                status = 404

        else:
            # Resource NOT FOUND
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