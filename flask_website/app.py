from flask import Flask
from flask_website.views.test_controller import test_controller
from flask_website.views.test_socket_io import socket_io,test_socket_io

app = Flask(__name__)
app.register_blueprint(test_controller)
app.register_blueprint(test_socket_io)

@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'

if __name__ == '__main__':
    socket_io.init_app(app)
    socket_io.run(app)
