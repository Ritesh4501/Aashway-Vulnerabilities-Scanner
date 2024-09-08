# Aashway Port/Vulnerability Scanner

A simple and fast Python-based port scanner with multi-threading support. This tool scans a target IP or domain for open ports and identifies the common protocols associated with those ports.

## Features

- **Multi-threading**: Utilizes threading to speed up the scanning process by scanning multiple ports simultaneously.
- **Protocol Detection**: Identifies and returns the common protocol associated with an open port.
- **User Input**: Takes target IP or domain as input.
- **Completion Notification**: Displays a message when the scan is completed with a timestamp.
- **Error Handling**: Gracefully handles errors like host not found, connection timeout, and keyboard interruption.

## Installation

### Prerequisites

- Python 3.x
- `pyfiglet` module for ASCII banners
- No additional libraries are required except for the built-in `socket`, `threading`, and `queue`.

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/port-scanner.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd port-scanner
   ```

3. **Install Dependencies**:
   Install `pyfiglet` via `pip`:
   ```bash
   pip install pyfiglet
   ```

4. **Run the Script**:
   ```bash
   python main.py <target_ip_or_domain>
   ```

   Example:
   ```bash
   python main.py google.com
   ```

## How to Use

1. **Target Specification**: The script requires the target IP address or domain as an argument when running the script.
   
   Example:
   ```bash
   python main.py <target_ip_or_domain>
   ```

2. **Port Scanning**: The program scans all ports in the range from 1 to 65535. For every open port found, it displays the port number and the protocol associated with it.

3. **Scan Output**: The script will print which ports are open and the associated protocol if known. It will also notify when the scan is finished.

Example output:

```bash
--------------------------------------------------
Scanning Target: 192.168.1.1
Scanning started at: 2024-09-07 18:00:00
--------------------------------------------------
Port 22 is open (SSH)
Port 80 is open (HTTP)
Port 443 is open (HTTPS)
--------------------------------------------------
Scanning finished at: 2024-09-07 18:05:35
Scan complete. All ports have been scanned.
--------------------------------------------------
```

## Project Structure

```
port-scanner/
│
├── main.py           # Main Python script for the port scanner
└── README.md         # Documentation for the project
```

## Error Handling

- **Keyboard Interrupt**: Pressing `Ctrl + C` will safely stop the scan.
- **Hostname Resolution Error**: If the target hostname cannot be resolved, an error will be shown.
- **Server Response Error**: If the server is not responding, the program will display an appropriate message.

## Performance Tuning

The number of threads (`num_threads`) can be modified in the `main.py` script to balance performance. Increasing the number of threads will make the scanning faster but could overwhelm the system if set too high.

```python
num_threads = 100  # Number of concurrent threads for scanning
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

