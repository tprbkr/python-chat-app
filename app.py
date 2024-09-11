from flask import Flask, render_template, request, redirect, send_from_directory, url_for
from flask_socketio import SocketIO, send
import os


app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Route to serve the favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
    'favicon.ico', mimetype='image/vnd.microsoft.icon')

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
