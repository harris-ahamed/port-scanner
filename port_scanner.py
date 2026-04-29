import socket

target = "10.0.2.2"

for port in range(1, 1001):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    print("Checking port " + str(port))
    result = s.connect_ex((target, port))
    if result == 0:
        print("Port " + str(port) + " is OPEN!")
    s.close()

