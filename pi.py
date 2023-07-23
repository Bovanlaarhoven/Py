import paramiko
import time

host = '192.168.2.13'
username = 'pi'
password = 'Pi'

successful_connections = 0
num_iterations = 10

for i in range(1, num_iterations + 1):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, username=username, password=password)
        command = 'curl -s "https://visitcount.itsvg.in/api?id=Robobo2022"'
        stdin, stdout, stderr = ssh.exec_command(command)

        output = stdout.read().decode().strip()
        if output:
            successful_connections += 1
            print(f"\rSuccessfully connected to the website - Attempt {i}/{num_iterations}", end="")
        else:
            print(f"\rConnection failed - Attempt {i}/{num_iterations}", end="")

    finally:
        try:
            ssh.close()
        except Exception as e:
            print(f"\rError while closing the SSH connection: {e}", end="")
    
    time.sleep(0.5) 

print(f"\nNumber of successful connections out of {num_iterations}: {successful_connections}")
