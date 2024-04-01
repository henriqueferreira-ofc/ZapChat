# site com os scripts: https://cdnjs.com/
#from distutils.command.install import install
#pip install python-socketio flask-socketio simple-websocket
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


# Funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)


# criar a nossa 1 pagina  = 1 rota
@app.route("/")  # decorator
def homepage():
    return render_template("index.html")


if __name__ == '__main__':
    socketio.run(app, host="192.168.1.7", allow_unsafe_werkzeug=True)




