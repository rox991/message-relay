import socket

# Replace these with the victim's IP and desired port
HOST = "0.0.0.0"  # Listens on all network interfaces
PORT = 4444        # Port to listen on

# Create a socket and bind it
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)  # Wait for one connection

print(f"Waiting for connection on {HOST}:{PORT}...")

# Accept the connection
conn, addr = sock.accept()
print(f"Connected to {addr}")

# Receive and print the message
data = conn.recv(1024)
print(f"Received message: {data.decode()}")

# Close the connection
conn.close()
