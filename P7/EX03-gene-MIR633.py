import http.client
import json
import termcolor

GENES = {"FRAT1" : "ENSG00000165879", "ADA": "ENSG00000196839",
         "FXN": "ENSG00000165060","RNU6-269P": "ENSG00000212379",
         "MIR633": "ENSG00000207552","TTTY4C": "ENSG00000228296",
         "RBMY2YP": "ENSG00000227633","FGFR3": "ENSG00000068078",
         "KDR": "ENSG00000128052","ANK2": "ENSG00000145362"}


Gene_name ="MIR633"
Server = "rest.ensembl.org"
Endpoint ="/sequence/id/"
Parameters ="?content-type=application/json"
Request_line = Endpoint + GENES[Gene_name] + Parameters
URL = Server + Request_line

print(f"Server: {Server}")
print(f"URL: {URL}")



# Connect with the server
conn = http.client.HTTPConnection(Server)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", Request_line)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
gene = json.loads(data1)

# Print the information in the object
print()
termcolor.cprint("Gene: ", 'green', end="")
print(Gene_name)

termcolor.cprint("Description: ", 'green', end="")
print(gene["desc"])
termcolor.cprint("Bases: ", 'green', end="")
print(gene["seq"])
