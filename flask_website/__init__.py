# 初始化flask 的位置
from flask import Flask
from flask_socketio import SocketIO
from flask_apscheduler import APScheduler


def init_app():
    app = Flask(__name__)
    return app


def init_socket_io(app):
    """
    记录：对于websocket 的实现
            threading 和 gevent 都使用长连接实现websocket的功能
            eventlet 实现了websocket的交互方式，但在使用非eventlet产生的线程发送消息的时候会产生问题
    """
    socket_io = SocketIO(async_mode='gevent') #eventlet , threading , gevent
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
