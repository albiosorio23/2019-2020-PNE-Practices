from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

# -- Cofigure the client
c = Client(IP, PORT)
print(c)

#print("Connection to SERVER at", IP, ", PORT: ", PORT)

# Test PING
print("* Testing PING...")
print(c.talk("PING"))

# Test GET
print("* Testing GET...")
print("GET 0:", c.talk("GET 0"))
print("GET 1:", c.talk("GET 1"))
print("GET 2:", c.talk("GET 2"))
print("GET 3:", c.talk("GET 3"))
print("GET 4:", c.talk("GET 4"))

# Test "INFO"
# We are going to use the sequence GET 0
print ("* Testing INFO...")
print(c.talk("INFO" + c.talk("GET 0")))

# Test "COMP"
print("* Testing COMP...")
print(c.talk("COMP" + c.talk("GET 0")))

# Test "REV"
print("* Testing REV...")
print(c.talk("REV" + c.talk("GET 0")))

# Test "GENE"
print("* Testing GENE...")
for gene in ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]:
    print("GENE" + c.talk(gene))


