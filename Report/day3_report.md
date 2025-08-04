# Day 3 Report – Port Scanning & Service Enumeration

**Device:** Google Home (10.0.x.x)  
**Network:** 10.0.0.0/x (Private LAN)  
**Tools Used:** Nmap (7.94), ARP, MAC Vendor Lookup

---

## 1️⃣ Objective
The goal of Day 3 was to:
- Identify open ports on the Google Home device.
- Enumerate running services.
- Analyze the device’s network exposure.
- Build foundational skills for IoT security testing.

---

## 2️⃣ Setup & Preparation
- Verified device IP using:
  ```bash
  arp -a
Result: Google Home is 10.0.x.x.

Confirmed connectivity using:

bash
Copy
Edit
ping 10.0.x.x
Result: Device responded successfully.

Nmap Scanning
3.1 Host Discovery
bash
Copy
Edit
nmap -sn 10.0.x.x
Purpose: Check if the device is online.
Result:

csharp
Copy
Edit
Host is up (0.0050s latency).
3.2 Full Port Scan
bash
Copy
Edit
nmap -p- 10.0.x.x
Purpose: Scan all 65,535 ports.
Result: Only a few open ports detected.

3.3 Service Enumeration
bash
Copy
Edit
nmap -sV 10.0.x.x
Purpose: Identify service details and versions.

Output:
Port	State	Service	Version
80	open	http	Google HTTP Server
443	open	ssl/https	TLSv1.3
8009	open	ajp13?	Unknown
9000	filtered	unknown	-

4️⃣ Interpretation of Results
Port 80 (HTTP)
Open for local device communication.

Service identified as Google HTTP Server.

Accessible only on the LAN.

No cloud exposure.

Port 443 (HTTPS)
Open and secured with TLSv1.3.

Confirms encrypted cloud-bound communication.

Matches findings from Day 2 TLS analysis.

Port 8009 (AJP?)
Open but uncertain protocol (marked ?).

Likely a Chromecast or proprietary Google service for local device coordination.

Port 9000 (Filtered)
Filtered by firewall, no response returned.

Device security is actively blocking unwanted scans.

Closed Ports
Other ports (e.g., 53) reported closed, confirming a minimal attack surface.

5️⃣ Key Findings
Device is reachable on the LAN.

Exposed ports are minimal and expected for its functionality.

TLSv1.3 is used for secure communication.

Proprietary port (8009) does not indicate an immediate risk but should be documented.

Firewall filtering further reduces the attack surface.

6️⃣ Visual Diagram
plaintext
Copy
Edit
[ Google Home (10.0.x.x) ]
         │
         │ Ports: 80 (HTTP), 443 (HTTPS), 8009 (Proprietary)
         │
   [ Local Network 10.0.x.x ]
         │
         ▼
 [ Secure TLS 1.3 Cloud Connection ]
✅ Conclusion
Day 3 successfully confirmed:

Minimal open ports on the Google Home device.

Strong encryption for cloud traffic via TLSv1.3.

Proper use of firewall filtering for non-essential ports.

No unexpected or insecure services detected.

The Google Home device shows a secure default configuration suitable for consumer IoT.