import paramiko
# import sys
# import os
# import os.path
# import cmd

# ip = '192.168.9.97'
# port = 22
# username = 'premalatha'
# password = 'premalatha'
#
# cmd = 'pwd'
#
# paramiko.util.log_to_file("/home/kirankumar/Desktop/client.log")
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect("192.168.9.97", username="premalatha", password=password)
# print ("Connected to {0}".format(username))
#
# stdin, stdout, stderr = ssh.exec_command(cmd)
# outlines = stdout.readlines()
# res = ' '.join(outlines)
# ssh.close()
# print res

# Connecting to Server
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print ("Please Enter the Remote machine details")
hostname = raw_input("Enter the ip: ")
port = input("Please enter the Port: ")
username = raw_input("Please enter the UserName: ")
password = raw_input("Please enter the Password: ")
cmd = raw_input("Enter the command to execute in the Remote Machine: ")
ssh.connect(hostname=hostname, port=port, username=username, password=password)
print ("Connected to {0}".format(username))
stdin, stdout, stderr = ssh.exec_command(cmd)
out = stdout.read()
print(out.decode())
ssh.close()
