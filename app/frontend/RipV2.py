#Aqui van los cosos de paramiko
import paramiko
import time

#conecta
def conecta(host):
    username = "cisco"
    password = "cisco"
    
    print("Conecta con "  + host)
    
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
        "show ip int brie",
        "conf t",
        "router rip",
        "version 2",
        "network 148.204.0.0",
        "network 8.0.0.0",
        "end",
        "wr",
        "telnet 8.8.8.1",
        "cisco",
        "cisco",
        "show ip int brie",
        "conf t",
        "router rip",
        "version 2",
        "network 148.204.0.0",
        "network 8.0.0.0",
        "end",
        "wr",
        "telnet 8.8.8.6",
        "cisco",
        "cisco",
        "show ip int brie",
        "conf t",
        "router rip",
        "version 2",
        "network 148.204.0.0",
        "network 8.0.0.0",
        "end",
        "wr"
    ]
    DEVICE_ACCESS = session.invoke_shell()
    
    for command in comandosR1:
        DEVICE_ACCESS.send(f'{command}\n')
        print("Comando enviado: " + command+ "\n")
        time.sleep(.5)
        output = DEVICE_ACCESS.recv(65000)
        print(output.decode)
    session.close()
    
#Pone RipV2 en R2
def RipR2():
    session = conecta("8.8.8.1")
    comandosR2 =[
        "show ip int bie",
        "conf t",
        "router rip",
        "version 2",
        "network 148.204.0.0",
        "network 8.0.0.0",
        "end",
        "wr"
    ]
    DEVICE_ACCESS = session.invoke_shell()
    
    for command in comandosR2:
        DEVICE_ACCESS.send(f'{command}\n')
        print("Comando enviado: " + command+ "\n")
        time.sleep(.5)
        output = DEVICE_ACCESS.recv(65000)
        print(output.decode)
    session.close()
    
#Pone RipV2 en R3
def RipR3():
    session = conecta("8.8.8.6")
    comandosR3 =[
        "show ip int bie",
        "conf t",
        "router rip",
        "version 2",
        "network 148.204.0.0",
        "network 8.0.0.0",
        "end",
        "wr"
    ]
    DEVICE_ACCESS = session.invoke_shell()
    
    for command in comandosR3:
        DEVICE_ACCESS.send(f'{command}\n')
        print("Comando enviado: " + command + "\n")
        time.sleep(.5)
        output = DEVICE_ACCESS.recv(65000)
        print(output.decode)
    session.close()
    
#Borra config
def BorraRip():
    routers = ["8.8.8.4", "8.8.8.17", "148.204.56.1"]
    comandosBorrar =[
        "show ip int bie",
        "conf t",
        "no router rip",
        "end",
        "wr"
    ]
    for router in routers:
        session = conecta(router)
        DEVICE_ACCESS = session.invoke_shell()
    
        for command in comandosBorrar:
            DEVICE_ACCESS.send(f'{command}\n')
            time.sleep(.5)
            output = DEVICE_ACCESS.recv(65000)
            print(output.decode)
        session.close()
        