import paramiko

from ftplib import FTP

import sys



# Replace these with your actual credentials

SSH_USERNAME = 'msfadmin'  # replace with your SSH username

SSH_PASSWORD = 'msfadmin'  # replace with your SSH password

FTP_USERNAME = 'msfadmin'   # replace with your FTP username

FTP_PASSWORD = 'msfadmin'    # replace with your FTP password



def ssh_connect(metasploitable_ip, port):

    try:

        # Create an SSH client

        client = paramiko.SSHClient()

        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        

        # Connect to the Metasploitable machine

        client.connect(metasploitable_ip, username=SSH_USERNAME, password=SSH_PASSWORD, port=port)

        print(f"Successfully connected to {metasploitable_ip} via SSH on port {port}.")

        

        # Open an interactive shell

        shell = client.invoke_shell()

        while True:

            command = input("Enter command to execute on Metasploitable (or 'exit' to quit): ")

            if command.lower() == 'exit':

                break

            shell.send(command + '\n')

            while shell.recv_ready():

                output = shell.recv(1024).decode('utf-8')

                print(output)

        

        client.close()

    except Exception as e:

        print(f"SSH Connection failed: {e}")



def ftp_connect(metasploitable_ip, port):

    try:

        # Create an FTP client

        ftp = FTP()

        ftp.connect(metasploitable_ip, port)

        ftp.login(user=FTP_USERNAME, passwd=FTP_PASSWORD)

        print(f"Successfully connected to {metasploitable_ip} via FTP on port {port}.")

        

        # List files in the current directory

        print("Files in the current directory:")

        ftp.retrlines('LIST')

        

        # Example: Downloading a file

        # ftp.retrbinary('RETR example.txt', open('example.txt', 'wb').write)

        

        ftp.quit()

    except Exception as e:

        print(f"FTP Connection failed: {e}")



def main():

    metasploitable_ip = input("Enter the IP address of the Metasploitable machine: ")

    port = int(input("Enter the port number (default for SSH is 22, for FTP is 21): "))

    

    print("Select connection type:")

    print("1. SSH")

    print("2. FTP")

    choice = input("Enter your choice (1/2): ")

    

    if choice == '1':

        ssh_connect(metasploitable_ip, port)

    elif choice == '2':

        ftp_connect(metasploitable_ip, port)

    else:

        print("Invalid choice.")



if __name__ == "__main__":

    main()

    

    

#Naveen_Wijesinghe 

    

