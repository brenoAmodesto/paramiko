from paramiko import SSHClient, AutoAddPolicy, sftp_client, transport
from paramiko import SFTPClient
import os
import paramiko.sftp_client

username = 'sftpuser'
password = 'user@15'
host = '192.168.1.146'
local_path = r'C:\Users\user\Documents\ssh\eita.py'
remote_path = '/home/sftpuser/folder'

transport = paramiko.Transport((host, 22))

transport.connect(username = username, password = password)

sftp = paramiko.SFTPClient.from_transport(transport)

#sftp.listdir(remote_path)

stdout = [sftp.lstat(remote_path), sftp.listdir(remote_path)]
s2 = stdout

for i in s2:
    print(i)

#sftp.stat(remote_path)
#sftp.put(local_path, os.path.join(local_path, remote_path))

#client = SSHClient()
#client.load_system_host_keys()
#client.connect(hostname=address, username=username, password=password)
#stdin, stdout, stderr = client.exec_command('ls /home/illi')

#print(stdout.readlines())
#stdout2 = stdout.readlines()

#for i in stdout2:
#    print(i)

#if client.connect:
#    print("Conectei nessa bucetinha gostosa")
#else: 
#    print("Você não conectou esse lixo")

#print(stdout.close)

#for line in stdout:
#    print(line)