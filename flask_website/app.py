from flask_website.views.test_controller import test_controller
from flask_website.views.test_socket_io import test_socket_io
from flask_website import socket_io, app

app.register_blueprint(test_controller)
app.register_blueprint(test_socket_io)


@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'


if __name__ == '__main__':
    socket_io.run(app)
