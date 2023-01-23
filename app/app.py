#import smtplib
import pexpect
from decouple import config
from flask import Flask

datos = 'cisco'
ipBusca = '148.204.56.1'

app = Flask(__name__)

@app.route('/')
def index():
	return "Holis"


@app.route('/f1')
def pruebaTelnet():
    child = pexpect.spawn('telnet ' + ipBusca)
    child.expect('Username:')
    child.sendline(datos)
    child.expect('Password:')
    child.sendline(datos)
    child.expect('R1#')
    child.sendline('exit')
    print("Mande los cosos")
    
    return "Mandado"


if __name__ == "__main__":
    #cosa = correo()
    pruebaTelnet()
    app.run(debug=True)