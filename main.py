#site com os scripts: https://cdnjs.com/
#from distutils.command.install import install
#pip install python-socketio flask-socketio simple-websocket
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

#Funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

# criar a nossa 1 pagina = 1 rota
@app.route("/")  # decorator
def homepage():
    return render_template("index.html")
app.debug = False

if __name__ == '__main__':
    host = "192.168.1.7"
    port = 5000
    print(f"Servidor Flask está sendo executado em http://192.168.1.7:5000/")
    socketio.run(app, host=host, port=port, debug=True, allow_unsafe_werkzeug=True)
    
