# SMBruteX
A simple Python tool for performing SMB brute-force attacks as part of a red team security assessment.


# SMBruteX 🔐

A simple Python-based brute-force tool designed for attacking SMB login services.  
This tool is built for red team assessments in a simulated lab environment.

---

## ⚙️ Features

- Brute-forces SMB login using wordlists
- Takes target IP input
- Loads usernames and passwords from `.txt` files
- Colorful terminal UI using `rich`
- Final result table in CLI

---

## 📦 Requirements

- Python 3
- `rich` library (install using `pip install rich`)

---

## 🛠️ How to Run

```bash
git clone https://github.com/yourusername/SMBruteX.git
cd SMBruteX
pip install rich
python smbrutex.py

