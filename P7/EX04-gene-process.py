import http.client
import json
import termcolor
from Seq1 import Seq

GENES = {"FRAT1" : "ENSG00000165879", "ADA": "ENSG00000196839",
         "FXN": "ENSG00000165060","RNU6-269P": "ENSG00000212379",
         "MIR633": "ENSG00000207552","TTTY4C": "ENSG00000228296",
         "RBMY2YP": "ENSG00000227633","FGFR3": "ENSG00000068078",
         "KDR": "ENSG00000128052","ANK2": "ENSG00000145362"}

Gene_name = input ("Write the gene name: ")

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

gene_seq = gene["seq"]
seq = Seq(gene_seq)
seq_length =len(gene_seq)

termcolor.cprint("Total length: ", 'green', end="")
print(seq_length)
number_of_A = seq.count_base("A")
percentage_A = "{:.1f}".format(100 * number_of_A / seq_length)
number_of_G = seq.count_base("G")
percentage_G = "{:.1f}".format(100 * number_of_G / seq_length)
number_of_T = seq.count_base("T")
percentage_T = "{:.1f}".format(100 * number_of_T / seq_length)
number_of_C = seq.count_base("C")
percentage_C = "{:.1f}".format(100 * number_of_C / seq_length)

termcolor.cprint("A", 'blue', end="")
print(f": {number_of_A} ({percentage_A}%)")
termcolor.cprint("C", 'blue', end="")
print(f": {number_of_C} ({percentage_C}%)")
termcolor.cprint("G", 'blue', end="")
print(f": {number_of_G} ({percentage_G}%)")
termcolor.cprint("T", 'blue', end="")
print(f": {number_of_T} ({percentage_T}%)")

value = 0
base = ""
for e, b in (seq.count()).items():
    # se empieza en 0, cada vez que va apareciendo una base se va sumando y queda ese valor como el mínimo
    while b > value:
        value = b
        base = e
termcolor.cprint("Most frequent Base: ", "green", end="")
print(base)


