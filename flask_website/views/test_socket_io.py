import time
from flask import Blueprint, render_template
from flask_socketio import emit
from flask_website import socket_io, scheduler

test_socket_io = Blueprint("socket_io", __name__, url_prefix='/test/socket_io')


@test_socket_io.route('/')
def index():
    return render_template('websocket.html')


@socket_io.on('client_event', namespace='/socket_io/test')
def client_msg(msg):
    emit('server_response', {'data': msg['data']})


@socket_io.on('connect_event', namespace='/socket_io/test')
def connected_msg(msg):
    emit('server_response', {'data': msg['data']})


def push_data():
    socket_io.emit('server_response', {'data': time.time()}, namespace='/socket_io/test')

@test_socket_io.route('/stop')
def stop():
    if scheduler.get_job('push_data'):
        scheduler.remove_job(id='push_data')
    return 'stop'


@test_socket_io.route('/start')
def start():
    if not scheduler.get_job('push_data'):
        scheduler.add_job(func=push_data, args=(), trigger='interval', seconds=3, id='push_data')
    return 'start'
