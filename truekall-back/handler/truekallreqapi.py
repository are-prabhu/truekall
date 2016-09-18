from flask.ext.restful import reqparse, abort, Api, Resource
from managers.config_manager import CallAPIInfo
from worker.plivocall import MissKall

parser = reqparse.RequestParser()
parser.add_argument('UserMail', type=str)
parser.add_argument('Name', type=str)
parser.add_argument('SourceNumber', type=str)
parser.add_argument('DestinationNumber', type=str)
parser.add_argument('Gender', type=str)
parser.add_argument('SecretWord', type=str)


class MissKallRequestHandler(Resource):
	def __init__(self):
		args = parser.parse_args()
		self.usermail = args['UserMail']
		self.name = args['Name']
		self.sourcenumber = args['SourceNumber']
		self.destinationnumber = args['DestinationNumber']
		self.gender = args['Gender']
		self.secretword = args['SecretWord']

	def post(self):
		print CallAPIInfo.callapi_secretword
		print self.secretword

		if str(CallAPIInfo.callapi_secretword) == str(self.secretword):
			MissKall().plivomisscall(self.sourcenumber,self.destinationnumber)
		else:
			return "{'498':'invalid secret word'}"

		return "{'200':'passed'}"


