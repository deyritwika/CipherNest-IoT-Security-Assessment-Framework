# 🔒 CipherNest – IoT Security Assessment Framework

CipherNest is a hands-on IoT security assessment project that focuses on **analyzing, visualizing, and reporting the security posture of smart home devices**.  
This project replicates a real-world security workflow—network reconnaissance, traffic analysis, vulnerability scanning, and dashboard visualization.

---

## 📌 Project Overview
- **Goal:** Evaluate IoT devices (e.g., smart speakers, bulbs) for secure configurations and potential attack surfaces.
- **Scope:** Local network analysis, port/service enumeration, TLS traffic inspection, and risk visualization.
- **Approach:** Practical, data-driven, and extensible for multi-device assessments.

---

## 🚀 Features
- Device discovery using `ARP` and `mDNS`.
- TLS handshake and SNI inspection for encryption validation.
- Port and service enumeration with Nmap.
- Risk scoring for each device.
- Interactive **Dash + Plotly dashboard**.
- Scalable JSON-based data model for adding more devices.
- Professional report-ready visual captures.

---

## 🛠 Tech Stack
- **Python 3.10+**
- Dash & Plotly (for interactive dashboard)
- Nmap (for scanning)
- Wireshark (for traffic analysis)
- JSON (data storage)

---

## 📂 Project Structure
CipherNest/
│
├── README.md # Project documentation
├── device_data.json # Masked sample data
├── dashboard.py # Dashboard code
├── requirements.txt # Python dependencies
├── captures/ # Redacted captures (Wireshark, dashboard, reports)
│ ├── dashboard.png
│ ├── tls_handshake.png
└── reports/ # Daily reports and findings
├── day1.md
├── day2.md
├── day3.md
└── final_report.md
