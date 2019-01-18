from flask import request

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

@app.before_request
def print_request_info():
    print("请求地址：" + str(request.path))
    print("请求方法：" + str(request.method))
    print("---请求headers--start--")
    print(str(request.headers).rstrip())
    print("---请求headers--end----")
    print("GET参数：" + str(request.args))
    print("POST参数：" + str(request.form))

if __name__ == '__main__':
    db.create_all()
    socket_io.run(app)


