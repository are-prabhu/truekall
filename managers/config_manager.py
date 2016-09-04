import yaml
import os
from gevent import lock

class Config():
    def __init__(self, fname="config.yaml"):
        self.load(fname)

    def load(self, fname):
        self.def_home_dir = os.environ.get("PHONESERVER_HOME_DIR", os.getcwd())
        default = os.path.join(self.def_home_dir, "config", fname)
        #print default

        self.config = os.environ.get("PHONESERVER_CONFIG", default)
        self.dataMap = yaml.load(open(self.config))
        #print self.dataMap

    def dump(self):
        print self.dataMap

class ConfigManager(object):
    config_obj = None
    _lock = lock.RLock()

    @classmethod
    def get_instance(cls, fname="config.yaml"):
        if not cls.config_obj:
            with cls._lock:
                if not cls.config_obj:
                    cls.config_obj = Config(fname)
        return cls.config_obj


########################## COUCH INFO ###########################

COUCH_CONFIG = 'couchdb_config'
COUCH_HOST = 'couchdb_host'
COUCH_PORT = 'couchdb_port'
COUCH_USER = 'couch_username'
COUCH_PASSWD = 'couch_password'
COUCH_FORMDB = 'front_caller_db'

class CouchInfo:
	config_obj = ConfigManager.get_instance()
        config = config_obj.dataMap
        envblock = config.get(COUCH_CONFIG,{})
	couch_host = str(envblock[COUCH_HOST])
	couch_port = str(envblock[COUCH_PORT])
	couch_user = str(envblock[COUCH_USER])
	couch_passwd = str(envblock[COUCH_PASSWD])
	couch_formdb = str(envblock[COUCH_FORMDB])
	










