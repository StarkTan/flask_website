import time
from flask import Blueprint, render_template
from flask_socketio import SocketIO, emit, send
from threading import Thread

test_socket_io = Blueprint("socket_io", __name__, url_prefix='/test/socket_io')
socket_io = SocketIO()


@test_socket_io.route('/')
def index():
    return render_template('websocket.html')

@socket_io.on('client_event', namespace='/socket_io/test')
def client_msg(msg):
    emit('server_response', {'data': msg['data']})


@socket_io.on('connect_event', namespace='/socket_io/test')
def connected_msg(msg):
    emit('server_response', {'data': msg['data']})


class DataPusher(Thread):
    def __init__(self):
        super().__init__()
        self.flag = False

    def run(self):
        while True:
            time.sleep(1)
            while self.flag:
                time.sleep(1)
                #socket_io.emit 和emit是不一样的
                socket_io.emit('server_response', {'data': time.time()}, namespace='/socket_io/test')
    def end(self):
        self.flag = False

    def begin(self):
        self.flag = True

pusher = None


@test_socket_io.route('/stop')
def stop():
    global pusher
    if pusher:
        pusher.end()
    return 'stop'


@test_socket_io.route('/start')
def start():
    global pusher
    if not pusher:
        pusher = DataPusher()
        pusher.start()
        pusher.begin()
    else:
        pusher.begin()
    return 'start'
