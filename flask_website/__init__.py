# 初始化flask 的位置
from flask import Flask
from flask_socketio import SocketIO


def init_app():
    app = Flask(__name__)
    return app


def init_socket_io():
    socket_io = SocketIO()
    return socket_io


app = init_app()
socket_io = init_socket_io()
socket_io.init_app(app)
