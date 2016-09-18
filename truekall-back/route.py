from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource
from managers.config_manager import CallAPIInfo
from handler.truekallreqapi import MissKallRequestHandler


app = Flask(__name__)
api = Api(app)

api.add_resource(MissKallRequestHandler,'/misskall/v1')

if __name__ == '__main__':
        app.run(
        host = CallAPIInfo.callapi_host,
	port = int(CallAPIInfo.callapi_port),
        debug=True
)


