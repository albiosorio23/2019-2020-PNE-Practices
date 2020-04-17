import http.client
import json

SERVER = "rest.ensembl.org"
Endpoint = "info/ping"
Parameters = "?content-type=application/json"
URL = SERVER + Endpoint + Parameters

print(f"Server: {SERVER}")
print(f"URL: {URL}")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", Endpoint + Parameters)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()
# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# Variable with the data1 in the form that we received (json)
response = json.loads(data1)

endpoint_ping = response["ping"]

# -- Print the received data
if endpoint_ping == 1:
    print("PING OK! The database is running!")