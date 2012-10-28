import os
from Error import QueryError
import json

class QueryConfig:
	query_file = None
	query_file_name = 'queries.json'
	query_list = None
	
	def __init__(self):
		self.loadFile()
		
	def loadFile(self):
		if not os.path.exists(self.query_file_name):
			fp = open(self.query_file_name, 'w')
			fp.close()
		
		try:
			self.query_file = open(self.query_file_name, 'r')
		except IOError:
			raise QueryError("Could not get custom queries", 1, QueryError.E_TYPE_CRITICAL)
		
		try:
			self.query_list = json.load(self.query_file)['queries']
		except ValueError:
			self.query_list = []
		
		self.query_file.close()
	
	def refresh(self):
		self.loadFile()
	
	def updateQuery(self, query_id):
		pass
	
	def deleteQuery(self, query_id):
		pass