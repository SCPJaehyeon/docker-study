import json
import logging
import requests
import urllib
import utils

from flask import Flask, redirect, render_template, request, url_for
from flask_restplus import Resource, Api, fields
from table import UserTable

flask_app = Flask(__name__)
api = Api(app=flask_app, version='1.0', title='WP User API', description='WP User API Site')


ns = api.namespace('userapi', description='Main APIs')
user_model = api.model('UserModel',
        {
            'id' : fields.Integer(required=True, description="user ID", help="BIGINT(20) UNSIGNED"),
            'user_login' : fields.String(required=True, description="login ID", help="VARCHAR(60)"),
            'user_pass': fields.String(required=True, description="login PW", help="VARCHAR(64) MD5"),
            'user_nicename' : fields.String(required=True, description="user Nice Name", help="VARCHAR(50)"),
            'user_email': fields.String(required=True, description="user Email", help="VARCHAR(100)"),
            'display_name': fields.String(required=True, description="user Display Name", help="VARCHAR(250)"),
        })
users_model = api.model('SitesModel',
        {
            'id' : fields.List(fields.Nested(user_model), description="user ID"),
            'count' : fields.Integer(min=0),
            'page': fields.Integer(min=0),
        })


api.parser().add_argument('page', type=int, help='Page', location='query')
api.parser().add_argument('itemsInPage', type=int, help='Items in page', location='query')


@ns.route('/users')
class List_Users(Resource):
    @api.expect(api.parser())
    @api.response(200, 'Success')
    @api.response(400, 'Validation Error')
    def get(self):
        return list_users()

@ns.route('/user')
class ADD_User(Resource):
    @api.expect(user_model, validate=False)
    @api.response(200, 'Success')
    def post(self):
        return add_user()

@ns.route('/user/<id>')
@api.doc(params={'id':'INPUT ID'})
class Site(Resource):
    @api.marshal_with(user_model, as_list=False)
    @api.response(200, 'Success')
    def get(self, id):
        return get_user(id)

    @api.response(200, 'Success')
    @api.expect(user_model, validate=False)
    def put(self, id):
        return update_user(id)

    @api.response(200, 'Success')
    def delete(self, id):
        return delete_user(id)

def list_users():
    page = int(request.args.get('page', "0"))
    num = int(request.args.get('itemsInPage', "10"))
    res = UserTable().users(page=page, itemsInPage=num)
    result = {
        "sites" : "{}".format(res),
        "count" : len(res),
        "page"  : page
    }
    print("INPUT > {}".format(result))
    return result

def add_user():
    j = request.get_json()
    print("INPUT > {}".format(j))
    result = UserTable().insert(j)
    result = {"message":"ok"} if result is None else result
    response = flask_app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    return response

def get_user(id):
    result = UserTable().user(id)
    return result

def update_user(id):
    j = request.get_json()
    result = UserTable().update(id,j)
    result = {"message":"ok"} if result is None else result
    response = flask_app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    return response

def delete_site(id):
    result = UserTable().delete(id)
    result = {"message":"ok"} if result is None else result
    response = flask_app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", debug=True, port=5000)

