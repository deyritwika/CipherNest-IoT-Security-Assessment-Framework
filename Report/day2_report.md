# Day 2 Report – IoT Wireless Security Analysis

**Device:** Google Home (10.0.x.x)  
**Network:** 10.0.0.0/x (Private LAN)  
**Tools Used:** Wireshark, ARP, MAC Vendor Lookup

---

## 1️⃣ mDNS & Device Discovery
- Captured **mDNS traffic** from Google Home on `UDP 5353`.
- Verified device advertisements:
  - **Service:** `_googlecast._tcp.local`
  - **IP:** `10.0.0.x`
  - **MAC Vendor:** Google LLC
- Confirmed local discovery of other Google devices (e.g., secondary Google Home speaker).

---

## 2️⃣ TLS Traffic Analysis

### Local TLS (LAN)
- **Source:** `10.0.x.x` (Google Home)  
- **Destination:** `10.0.x.x` (Google Home Speaker)  
- **Protocol:** TLSv1.3  
- **Handshake:** Client Hello observed  
- **Vendor Verification:** MAC Vendor = Google LLC  
- **Conclusion:** Secure encrypted device-to-device communication inside LAN.

### Cloud TLS
- **Source:** `10.0.0.x` (Google Home)  
- **Destination:** External Google servers (persistent TLS session)  
- **Protocol:** TLSv1.3  
- **Handshake:** No new Client Hello observed (likely persistent connection)  
- **Traffic:** Encrypted Application Data confirmed; no plaintext traffic detected  
- **Conclusion:** Google Home uses persistent secure TLS connections to Google Cloud.

---

## 3️⃣ Key Findings
- Google Home uses **TLS 1.3** for both **local device-to-device communication** and **cloud communication**.
- LAN communication is encrypted end-to-end; no plaintext data was visible.
- Persistent TLS sessions prevent frequent handshakes but maintain security.
- Network segmentation between LAN and cloud confirmed.

---

## 4️⃣ Visual Diagram
```plaintext
[ Google Home (10.0.x.x) ]
          │ (TLS 1.3 - Local)
          │
[ Google Home Speaker (10.0.x.x) ]

          │ (TLS 1.3 - Persistent Cloud Session)
          ▼
   [ Google Cloud Servers (Public IPs) ]
