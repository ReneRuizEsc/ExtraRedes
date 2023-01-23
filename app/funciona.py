import smtplib

def correo():
	message = "Soy un mensaje"

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login('juanissoldado@gmail.com', 'dtwifjckzysszdyk')
	server.sendmail('juanissoldado@gmail.com', 'muchfalsosuchwow@gmail.com', message)
	
	server.quit()
	print("Correo enviado")
 
	return "Mensaje de retorno"