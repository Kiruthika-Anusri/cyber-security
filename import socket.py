import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("Basic Network Sniffer")
print("---------------------")
print("Device Name:", hostname)
print("IP Address:", ip_address)

print("\nNetwork details captured successfully")
print("Protocol: TCP/IP")