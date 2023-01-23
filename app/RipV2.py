#Aqui van los cosos de paramiko
import paramiko
import time

#conecta
def conecta(host):
    username = "cisco"
    password = "cisco"
    
    session = paramiko.SSHClient()
    
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    session.connect(hostname=host, username=username, password=password)
    
    return session

#Pueba de conectividad
def pruebaPara():
    session = conecta("148.204.56.1")
    stdin, stdout, sterr = session.exec_command('show ip interface brief')
    time.sleep(.5)
    
    print(stdout.read().decode())
    
    session.close()

#Pone RipV2 en R1
def RipR1():
    session = conecta("148.204.56.1")
    comandosR1 =[
        "show ip int bie",
        "conf t",
        "router rip",
        "version 2",
        "network 148.204.56.0",
        "network 8.8.8.0",
        "end",
        "wr"
    ]
    DEVICE_ACCESS = session.invoke_shell()
    
    for command in comandosR1:
        DEVICE_ACCESS.send(f'{command}\n')
        time.sleep(.5)
        output = DEVICE_ACCESS.recv(65000)
        print(output.decode)
    session.close()
    
#Pone RipV2 en R2
def RipR2():
    session = conecta("8.8.8.17") #CAMBIAR ESTO CON LA TOPOLOGIA--------------------------------
    comandosR1 =[
        "show ip int bie",
        "conf t",
        "router rip",
        "version 2",
        "network 148.204.59.0",
        "network 8.8.8.0",
        "end",
        "wr"
    ]
    DEVICE_ACCESS = session.invoke_shell()
    
    for command in comandosR1:
        DEVICE_ACCESS.send(f'{command}\n')
        time.sleep(.5)
        output = DEVICE_ACCESS.recv(65000)
        print(output.decode)
    session.close()
    
#Pone RipV2 en R3
def RipR3():
    session = conecta("8.8.8.4")
    comandosR1 =[
        "show ip int bie",
        "conf t",
        "router rip",
        "version 2",
        "network 148.204.60.0",
        "network 8.8.8.0",
        "end",
        "wr"
    ]
    DEVICE_ACCESS = session.invoke_shell()
    
    for command in comandosR1:
        DEVICE_ACCESS.send(f'{command}\n')
        time.sleep(.5)
        output = DEVICE_ACCESS.recv(65000)
        print(output.decode)
    session.close()
    
#Borra config