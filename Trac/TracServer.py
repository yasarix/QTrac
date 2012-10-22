'''
@author: Yasar Senturk
'''

import xmlrpclib
import Error

class TracServer(object):
	'''
	This class maintains Trac server connection
	'''
	connection = None
	
	def __init__(self, server_address, username, password):
		'''
		Constructor
		'''
		self.server_address = server_address + "/login/xmlrpc"
		
		try:
			self.connection = xmlrpclib.ServerProxy("http://" + username + ":" + password + "@" + self.server_address)
		except:
			raise Error.ConnectionError("Could not connect to server " + "http://" + username + ":" + password + "@" + self.server_address)
