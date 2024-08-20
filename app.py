from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        return redirect(url_for('index_chat', username=username))
    return render_template('index.html')

@app.route('/chat')
def index_chat():
    username = request.args.get('username', 'Anonymous')
    return render_template('chat.html', username=username)

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
