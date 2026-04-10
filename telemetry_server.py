import socket
import time

HOST = "0.0.0.0"
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print("Telemetry server listening on port", PORT)

packet_count = 0
total_cpu = 0
total_temp = 0

# store last sequence number per client
last_seq = {}

start_time = time.time()

while True:
    data, addr = sock.recvfrom(1024)
    packet_count += 1

    message = data.decode()
    client_ip = addr[0]

    # Example message: SEQ:5 CPU:40 TEMP:32
    parts = message.split()

    seq = int(parts[0].split(":")[1])
    cpu = int(parts[1].split(":")[1])
    temp = int(parts[2].split(":")[1])

    # -------- Packet Loss Detection --------
    if client_ip in last_seq:
        if seq != last_seq[client_ip] + 1:
            lost = seq - last_seq[client_ip] - 1
            if lost > 0:
                print("Packet loss from", client_ip, "lost:", lost)

    last_seq[client_ip] = seq

    # -------- Aggregation --------
    total_cpu += cpu
    total_temp += temp

    avg_cpu = total_cpu / packet_count
    avg_temp = total_temp / packet_count

    print("\nPacket", packet_count, "from", client_ip)
    print("Telemetry:", message)
    print("Average CPU:", round(avg_cpu, 2))
    print("Average Temp:", round(avg_temp, 2))

    # -------- Performance Metric --------
    if packet_count % 20 == 0:
        elapsed = time.time() - start_time
        rate = packet_count / elapsed
        print("\n---- Performance ----")
        print("Packets received:", packet_count)
        print("Packets/sec:", round(rate, 2))
        print("---------------------")