import plivo
from managers.config_manager import PlivoInfo


class MissKall(object):
	def __init__(self):
		self.call_params={}
		self.answer_url = PlivoInfo.plivo_answer_url
		self.hang_onring =  PlivoInfo.plivo_hang_onring
		self.auth_token = PlivoInfo.plivo_auth_token
		self.auth_id = PlivoInfo.plivo_auth_id

	def plivomisscall(self,source,destination):
		self.call_params['from'] = source
		self.call_params['answer_method'] = 'POST'
		self.call_params['answer_url'] = self.answer_url
		self.call_params['to'] = destination
		self.call_params['hangup_on_ring'] = PlivoInfo.plivo_hang_onring

		triger_call = plivo.RestAPI(self.auth_id,self.auth_token)
		call_result = triger_call.make_call(self.call_params)
		print call_result
		


		
		

