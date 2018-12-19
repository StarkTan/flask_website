# 初始化flask 的位置
from flask import Flask
from flask_socketio import SocketIO
from flask_apscheduler import APScheduler


def init_app():
    app = Flask(__name__)
    return app


def init_socket_io(app):
    socket_io = SocketIO()
    socket_io.init_app(app)
    return socket_io


def init_scheduler(app):
    scheduler = APScheduler();
    scheduler.init_app(app)
    scheduler.start()
    return scheduler


app = init_app()
scheduler = init_scheduler(app)
socket_io = init_socket_io(app)
