import smtplib
import pexpect

def correo():
	message = "Soy un mensaje"

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login('juanissoldado@gmail.com', 'dtwifjckzysszdyk')
	server.sendmail('juanissoldado@gmail.com', 'muchfalsosuchwow@gmail.com', message)
	
	server.quit()
	print("Correo enviado")
 
	return "Mensaje de retorno"

def pruebaTelnet():
    datos = 'cisco'
    ipBusca = '148.204.56.1'
    
    child = pexpect.spawn('telnet ' + ipBusca)
    child.expect('Username:')
    child.sendline(datos)
    child.expect('Password:')
    child.sendline(datos)
    child.expect('R1#')
    child.sendline('exit')
    print("Mande los cosos")