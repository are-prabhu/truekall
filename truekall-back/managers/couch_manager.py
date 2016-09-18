from config_manager import ConfigManager,CouchInfo
import time
from couchdb import Server, Session
from gevent import lock
from couchdb.design import ViewDefinition


class CouchProperties:
	def __init__(self):
		pass

	def conn(self):
		couch_conn = Server('http://%s:%s' % (CouchInfo.couch_host,CouchInfo.couch_port))
		couch_conn.resource.credentials = (CouchInfo.couch_user,CouchInfo.couch_passwd)
		return couch_conn

class CouchManager(object):
	couch_obj = None
	_lock = lock.RLock()

	@classmethod
	def get_instance(cls):
		if not cls.couch_obj:
			with cls._lock:
				if not cls.couch_obj:
					cls.couch_obj = CouchProperties().conn()
		return cls.couch_obj

	@staticmethod
	def formdb_instance():
		return CouchManager.get_instance()[CouchInfo.couch_formdb]


class CouchOperations():
	def __init__(self):
		pass
	@staticmethod
	def couch_insert(insert_docs,db=CouchManager.formdb_instance()):
		db.save(insert_docs)

	def couch_update(self,db,rev_id,update_docs):
		db.save(update_docs)

	def couch_get_view(self,db,get_token):
		view = ViewDefinition('%sview' % db.name, '%s' % db.name, '''function(doc) {if (doc._id == "%s") emit(doc);}''' % get_token)
		view.sync(db)

		for res in db.view('_design/%sview/_view/%s' %(db.name,db.name) ):
			return {res.id:res.key}

#CouchOperations.couch_insert({"hi":"test"})
