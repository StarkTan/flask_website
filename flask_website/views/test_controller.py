from flask import Blueprint,Response,render_template

# url_prefix 前面要加斜杠
test_controller = Blueprint("controller", __name__, url_prefix='/test/controller')


@test_controller.route('/rest')
def rest_return():
    return Response('rest response', mimetype='application/json')

@test_controller.route('/html')
def html_retune():
    # 返回文件还可以使用 send_from_directory，send_static_file
    return render_template('test_html.html')

@test_controller.route('/data_html')
def html_data_return():
    u =[[3,2,1],[1,2,3],[2,1,3]]
    return render_template('test_html.html',u=u)