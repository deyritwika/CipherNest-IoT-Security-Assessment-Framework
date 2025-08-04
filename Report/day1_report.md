# Day 1 – IoT Wireless Security Project

## Objective
Establish the project setup, perform initial network discovery, and capture baseline traffic from a smart home device (Google Home).

---

## Tools Used
- **Wireshark** – For packet capture and analysis
- **Acrylic Wi-Fi Home** – For Wi-Fi scanning
- **Advanced IP Scanner** – For device discovery and MAC identification
- **Windows Command Prompt** – For basic ARP lookups

---

## Activities Completed
1. Created project folder structure:
Documents/iot-wireless-security/
├── captures/
├── notes/

2. Installed and configured Wireshark, Acrylic Wi-Fi, and Advanced IP Scanner.
3. Performed Wi-Fi scan and exported results (`network_scan_day1.csv`).
4. Mapped connected devices:
| Device Name     | IP Address     | MAC Address         | Protocols           |
|-----------------|---------------|--------------------|--------------------|
| Google Home     | 192.168.1.15  | AA:BB:CC:DD:EE:FF | Wi-Fi, mDNS, TLS   |
| Laptop         | 192.168.1.10  | 11:22:33:44:55:66 | Wi-Fi              |
| Smart Bulb 1   | 192.168.1.20  | 77:88:99:AA:BB:CC | Zigbee (via Hub)   |

5. Captured Google Home traffic:
- Observed **mDNS** announcements (`_googlecast._tcp.local`).
- Noted **TLS traffic** to Google cloud servers.
- Saved capture: `captures/google_home_idle.pcapng`.

6. Documented findings in this report.

---

## Key Findings
- Google Home regularly announces itself using **mDNS** (local network discovery).
- Detected encrypted **TLS traffic** confirming secure cloud communication.
- Baseline device inventory established for ongoing monitoring.

---

## Deliverables
- `captures/google_home_idle.pcapng` (Wireshark capture)
- `captures/network_scan_day1.csv` (Wi-Fi scan results)
- `devices.md` (Device inventory)
- Google Home network diagram

---

## Next Steps
- Analyze captured mDNS packets for detailed device metadata.
- Explore SSDP traffic for additional IoT device discovery.
- Begin basic security evaluation (open port scanning).
- Start preparing a simple dashboard for visualizing device data.

---


