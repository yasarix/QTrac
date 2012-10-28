class Error(BaseException):
	message = None
	code = 0
	error_type = None
	
	E_TYPE_NOTICE = 1
	E_TYPE_MEDIUM = 2
	E_TYPE_CRITICAL = 3
	
	def __init__(self, *args):
		self.message = args[0]
		self.code = args[1]
		self.error_type = args[2] 
		self.args = args

class ConnectionError(Error):
	pass

class FileError(Error):
	pass

class QueryError(Error):
	pass