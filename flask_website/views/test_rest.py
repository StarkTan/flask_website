"""
测试数据库集成，rest 接口发布 restApi 文档书写
"""
from flask import Blueprint, Response, request, jsonify
from flask_website import db
from flask_website.utils import gen_id

test_rest = Blueprint("rest", __name__, url_prefix='/test/rest/user')


class User(db.Model):
    id = db.Column(db.String(32), default=gen_id, primary_key=True)
    name = db.Column(db.String(99), unique=True)
    name_cn = db.Column(db.String(99), unique=False)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'User %r' % self.name


@test_rest.route('/', methods=["GET"])
def get():
    """Del some data

       @@@
       #### args

       | args | nullable | type | remark |
       |--------|--------|--------|--------|
       |    title    |    false    |    string   |    blog title    |
       |    name    |    true    |    string   |    person's name    |

       #### return
       - ##### json
       > {"msg": "success", "code": 200}
       @@@
    """
    users = db.session.query(User).all()
    return jsonify(str(users))


@test_rest.route('/', methods=["POST"])
def post():
    name = request.form['name']
    age = request.form['age']
    user = User(name, int(age))
    db.session.add(user)
    db.session.commit()
    return jsonify(str(True))
