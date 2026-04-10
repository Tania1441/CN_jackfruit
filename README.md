#  Secure Telemetry System using TLS & UDP

##  Overview

This project implements a **secure and scalable telemetry system** using a hybrid communication model:

* **TLS (TCP)** for secure control communication
* **UDP** for fast telemetry data transfer

The system is designed to achieve **low latency, high throughput, and scalability** while maintaining necessary security.

---

##  System Architecture

Client → Control Server (TLS) → Telemetry Server (UDP)

### Components:

* **Client**

  * Connects securely to Control Server
  * Receives configuration
  * Sends telemetry data via UDP

* **Control Server**

  * Uses TLS for secure communication
  * Provides telemetry server details to clients

* **Telemetry Server**

  * Receives telemetry data
  * Performs packet loss detection
  * Computes performance metrics

---

##  Features

*  Secure configuration exchange using TLS
*  High-speed telemetry using UDP
*  Sequence-based packet loss detection
*  Real-time performance metrics (throughput, averages)
*  Modular and scalable architecture

---

##  How to Run

### Step 1: Generate Certificate

```bash
python generate_cert.py
```

### Step 2: Start Control Server

```bash
python control_server.py
```

### Step 3: Start Telemetry Server

```bash
python telemetry_server.py
```

### Step 4: Run Client

```bash
python client.py
```

---

##  Performance Evaluation

The system evaluates performance using:

* **Throughput** → packets per second
* **Packet Loss** → detected via missing sequence numbers
* **Average CPU & Temperature** → computed in real-time

Example:

* Stable performance with single client
* Increased packet rate with multiple clients
* Packet loss observed under high load

---

##  Scalability

The system is designed for scalability:

* Uses **UDP** → no connection overhead
* **Stateless telemetry server** → handles multiple clients independently
* **Minimal per-client storage** → only sequence numbers tracked
* **Constant-time processing** → efficient under high load
* **Modular architecture** → components can scale independently

---

##  Optimization Techniques

The following optimizations are implemented:

* **UDP-based communication** for low latency
* **Selective TLS usage** (only for control, not telemetry)
* **Lightweight message format** (plain string instead of JSON/XML)
* **Sequence numbers instead of ACKs** to reduce network overhead
* **Incremental aggregation** (no full data storage)
* **Controlled transmission rate** to avoid congestion

---

##  Failure Handling

The system demonstrates handling of:

* **Packet Loss**

  * Detected using sequence numbers

* **High Load / Congestion**

  * Leads to observable packet loss

* **Control Server Dependency**

  * Client requires config before sending data

---

## Technologies Used

* Python
* Socket Programming
* SSL/TLS (cryptography library)
* UDP & TCP networking

---

##  Conclusion

This project demonstrates a **secure, efficient, and scalable telemetry system** by combining:

* Secure control communication (TLS)
* Fast data transmission (UDP)
* Lightweight processing and monitoring

---

##  Authors

* Keertika Acharya
* Madhuri
* Khushi Paraddi
