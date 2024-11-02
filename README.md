# Remote_Access

# Metasploitable SSH & FTP Connector

A Python script to connect to a Metasploitable machine using SSH and FTP protocols. This tool allows users to execute commands interactively over SSH and manage files via FTP.

## Features

- **SSH Connection**: 
  - Connect to a Metasploitable machine using SSH credentials.
  - Execute commands interactively in a shell environment.

- **FTP Connection**: 
  - Connect to the Metasploitable machine using FTP credentials.
  - List files in the current directory.
  - (Optional) Download files from the server.

## Requirements

- Python 3.x
- [Paramiko](https://pypi.org/project/paramiko/) library

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/metasploitable-connector.git
   cd metasploitable-connector
   ```

2. **Install Dependencies**
   ```bash
   pip install paramiko
   ```

## Usage

1. **Configure Credentials**
   
   Update the script with your SSH and FTP credentials:
   ```python
   SSH_USERNAME = 'your_ssh_username'
   SSH_PASSWORD = 'your_ssh_password'
   FTP_USERNAME = 'your_ftp_username'
   FTP_PASSWORD = 'your_ftp_password'
   ```

2. **Run the Script**
   ```bash
   python connector.py
   ```

3. **Follow the Prompts**
   - Enter the IP address of the Metasploitable machine.
   - Specify the port number (default: 22 for SSH, 21 for FTP).
   - Choose the connection type (SSH or FTP).

## Security Notice

**Warning:** Storing credentials in plain text is insecure. Consider using environment variables or a secure credential manager for sensitive information.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Disclaimer:** Use this tool responsibly and only on networks and systems you have permission to test.
