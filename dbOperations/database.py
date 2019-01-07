from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import logging


class CassandraOperations:

    def __init__(self):
        self.cluster = None
        self.session = None
        self.keyspace = None
        self.log = None

    def __del__(self):
        self.cluster.shutdown()

    def createSession(self,host):
        self.cluster = Cluster(['127.0.0.1'])
        self.session = self.cluster.connect(self.keyspace)

    def getSession():
        return self.session

    def setLogger(self,logLevel):
        log = logging.getLogger()
        log.setLevel(logLevel)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s :%(message)s"))
        log.addHandler(handler)
        self.log = log

    def createKeyspaceIfNotExists(self,keyspace):
        self.log.info("creating keyspace...")
        self.session.execute("""CREATE KEYSPACE IF NOT EXISTS %s with replication={'class':'SimpleStrategy','replication_factor':3}""" %keyspace)
        self.log.info("setting keyspace...")
        self.session.set_keyspace(keyspace)

    def executeQuery(self,query):
        self.log.info("executing query : %s .."%query)
        self.session.execute(query)

    def checkIfUserRegistered(self,teamName):
        self.log.info("checking whether team:"+teamName+" is registered or not")
        entries =  self.session.execute("SELECT * from workshop.student_entries where teamName='"+teamName+"';")
        if not entries:
            return False
        return True
