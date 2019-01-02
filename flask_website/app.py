from flask_website.views.test_rest import test_rest
from flask_website.views.test_controller import test_controller
from flask_website.views.test_socket_io import test_socket_io
from flask_website import socket_io, app,db

app.register_blueprint(test_controller)
app.register_blueprint(test_socket_io)
app.register_blueprint(test_rest)


@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'


if __name__ == '__main__':
    db.create_all()
    socket_io.run(app)
