import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print "Please fill the details carefully"
hostname = raw_input("Enter the receiver ip: ")
port = input("Please enter the receiver Port: ")
username = raw_input("Please enter the receiver UserName: ")
password = raw_input("Please enter the receiver Password: ")

ssh.connect(hostname=hostname, port=port, username=username, password=password)
print "Connected to {0}".format(username)

filepath = raw_input("Enter the file path with file name: ")
destpath = raw_input("Enter the destination path: ")
cmd = 'scp -r {0} {1}@{2}:{3}'.format(filepath, username, hostname, destpath)
print cmd
ssh.exec_command(cmd)
ssh.close()