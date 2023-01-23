#Aqui van los cosos de RIPv2
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

def ospfR():
    session = conecta("148.204.56.1")
    comandosR1 =[
        "show ip int brie",
        "conf t",
        "router ospf 1",
        "network 148.204.56.10 0.0.0.255 area 1",
        "network 8.8.8.2 0.0.0.3 area 1",
        "end",
        "wr",
        "telnet 8.8.8.1",
        "cisco",
        "cisco",
        "show ip int brie",
        "conf t",
        "router ospf 1",
        "network 148.204.59.10 0.0.0.255 area 1",
        "network 8.8.8.1 0.0.0.3 area 1",
        "network 8.8.8.5 0.0.0.3 area 1",
        "end",
        "wr",
        "telnet 8.8.8.6",
        "cisco",
        "cisco",
        "show ip int brie",
        "conf t",
        "router ospf 1",
        "network 148.204.60.10 0.0.0.255 area 1",
        "network 8.8.8.6 0.0.0.3 area 1",
        "end",
        "wr"
    ]
    DEVICE_ACCESS = session.invoke_shell()
    
    for command in comandosR1:
        DEVICE_ACCESS.send(f'{command}\n')
        print(" " + command+ "\n")
        time.sleep(.5)
        output = DEVICE_ACCESS.recv(65000)
        print(output.decode())
    session.close()
    
    return "OSPF en routers"

def BorraOSPF():
    comandosBorrar =[
        "telnet 8.8.8.1",
        "cisco",
        "cisco",
        "telnet 8.8.8.6",
        "cisco",
        "cisco",
        "show ip int brie",
        "conf t",
        "no router ospf 1",
        "end",
        "wr",
        "exit",
        "show ip int brie",
        "conf t",
        "no router ospf 1",
        "end",
        "wr",
        "exit",
        "show ip int brie",
        "conf t",
        "no router ospf 1",
        "end",
        "wr"
    ]
    session = conecta("148.204.56.1")
    DEVICE_ACCESS = session.invoke_shell()

    for command in comandosBorrar:
        DEVICE_ACCESS.send(f'{command}\n')
        time.sleep(.5)
        output = DEVICE_ACCESS.recv(65000)
        print(output.decode())
    session.close()
    
    return "OSPF quitado"