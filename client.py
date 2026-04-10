import socket
import ssl
import time
import random

CONTROL_SERVER_IP = "10.20.201.219"   # server laptop IP
CONTROL_PORT = 6000

# ---- TLS connection to control server ----
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
secure_sock = context.wrap_socket(sock)

print("Connecting to control server...")

secure_sock.connect((CONTROL_SERVER_IP, CONTROL_PORT))

config = secure_sock.recv(1024).decode()
print("Received config:", config)

secure_sock.close()

# Example config received:
# TELEMETRY_SERVER 192.168.137.152 5000
_, SERVER_IP, SERVER_PORT = config.split()
SERVER_PORT = int(SERVER_PORT)

# ---- UDP socket for telemetry ----
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Sending telemetry to", SERVER_IP, SERVER_PORT)

seq = 0

while True:
    seq += 1

    cpu = random.randint(10, 90)
    temp = random.randint(20, 50)

    message = f"SEQ:{seq} CPU:{cpu} TEMP:{temp}"

    udp.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

    print("Sent:", message)

    # faster sending for high-rate packet ingestion
    time.sleep(2)