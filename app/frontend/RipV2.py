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

#Pueba de conectividad
def pruebaPara():
    session = conecta("148.204.56.1")
    stdin, stdout, sterr = session.exec_command('show ip interface brief')
    time.sleep(.5)
    
    print(stdout.read().decode())
    
    session.close()
    
def genRouter(ipE): #Con la ip de entrada y aquí debajo la cadena agrega más routers
    session = conecta(ipE)
    listaTelnet = ["8.8.8.1","8.8.8.6"]
    comandosR1 =[
        "show ip int brie",
        "conf t",
        "router rip",
        "version 2",
        "network 148.204.56.0",
        "network 8.0.0.0",
        "no auto-summary",
        "end",
        "wr"
    ]
    
    for listaT in listaTelnet:
        comandoT = [
        "telnet {listaT}",
        "cisco",
        "cisco",
        "show ip int brie",
        "conf t",
        "router rip",
        "version 2",
        "network 148.204.60.0",
        "network 8.0.0.0",
        "no auto-summary",
        "end",
        "wr"]
        comandosR1.extend(comandoT)
        
    DEVICE_ACCESS = session.invoke_shell()
    
    for command in comandosR1:
        DEVICE_ACCESS.send(f'{command}\n')
        print("Comando enviado: " + command+ "\n")
        time.sleep(.5)
        output = DEVICE_ACCESS.recv(65000)
        print(output.decode())
    session.close()
    
    return "Rip en routers"

#Pone RipV2 en R1
def RipR():
    session = conecta("148.204.56.1")
    comandosR1 =[
        "show ip int brie",
        "conf t",
        "router rip",
        "version 2",
        "network 148.204.56.0",
        "network 8.0.0.0",
        "no auto-summary",
        "end",
        "wr",
        "telnet 8.8.8.1",
        "cisco",
        "cisco",
        "show ip int brie",
        "conf t",
        "router rip",
        "version 2",
        "network 148.204.59.0",
        "network 8.0.0.0",
        "no auto-summary",
        "end",
        "wr",
        "telnet 8.8.8.6",
        "cisco",
        "cisco",
        "show ip int brie",
        "conf t",
        "router rip",
        "version 2",
        "network 148.204.60.0",
        "network 8.0.0.0",
        "no auto-summary",
        "end",
        "wr"
    ]
    DEVICE_ACCESS = session.invoke_shell()
    
    for command in comandosR1:
        DEVICE_ACCESS.send(f'{command}\n')
        print("Comando enviado: " + command+ "\n")
        time.sleep(.5)
        output = DEVICE_ACCESS.recv(65000)
        print(output.decode())
    session.close()
    
    return "Rip en routers"

#Borra config
def BorraRip():
    comandosBorrar =[
        "telnet 8.8.8.1",
        "cisco",
        "cisco",
        "telnet 8.8.8.6",
        "cisco",
        "cisco",
        "show ip int brie",
        "conf t",
        "no router rip",
        "end",
        "wr",
        "exit",
        "show ip int brie",
        "conf t",
        "no router rip",
        "end",
        "wr",
        "exit",
        "show ip int brie",
        "conf t",
        "no router rip",
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
    
    return "Rip quitado"