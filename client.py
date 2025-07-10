# client.py
import socket

host = "10.21.42.23"  # Replace with your phone's IP
port = 12345

s = socket.socket()
s.connect((host, port))

command = "open whatsapp"
s.send(command.encode())

print(f"Sent: {command}")
s.close()
