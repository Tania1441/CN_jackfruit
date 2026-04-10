import socket
import ssl

HOST = "0.0.0.0"
PORT = 6000

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(5)

print("Control server running...")

while True:
    client, addr = sock.accept()
    secure_conn = context.wrap_socket(client, server_side=True)

    print("Client connected:", addr)

    message = "TELEMETRY_SERVER 192.168.137.251 5000"
    secure_conn.send(message.encode())

    secure_conn.close()