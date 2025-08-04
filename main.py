#site com os scripts: https://cdnjs.com/
#from distutils.command.install import install
#pip install python-socketio flask-socketio simple-websocket
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    print(f"Mensagem recebida: {mensagem}")
    send(mensagem, broadcast=True)
    print(f"Mensagem enviada para todos os clientes")

@socketio.on("connect")
def handle_connect():
    print("Cliente conectado")

@socketio.on("disconnect")
def handle_disconnect():
    print("Cliente desconectado")

# criar a nossa 1 pagina = 1 rota
@app.route("/")  # decorator
def homepage():
    return render_template("index.html")
app.debug = False

if __name__ == '__main__':
    host = "127.0.0.1"
    port = 5001
    print(f"Servidor Flask está sendo executado em http://127.0.0.1:5001/")
    socketio.run(app, host=host, port=port, debug=True, allow_unsafe_werkzeug=True)



