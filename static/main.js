var socket = io();
var username = '';

socket.on('message', function(msg) {
    var item = document.createElement('div');
    item.textContent = msg;
    document.getElementById('messages').appendChild(item);
});

function setUsername() {
    username = document.getElementById('username').value;
    document.getElementById('username').disabled = true;
}

function sendMessage() {
    var msg = document.getElementById('message').value;
    socket.send(username + ': ' + msg);
    document.getElementById('message').value = '';
}
