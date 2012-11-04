from PyQt4 import QtGui
from Error import *

class MessageBox(QtGui.QMessageBox):
	def __init__(self):
		super(MessageBox, self).__init__()
		pass
	
	def showMessageWithError(self, error_object):
		self.setText(error_object.message)
		
		if error_object.error_type == Error.E_TYPE_NOTICE:
			self.setIcon(self.Information)
		elif error_object.error_type == Error.E_TYPE_MEDIUM:
			self.setIcon(self.Warning)
		elif error_object.error_type == Error.E_TYPE_CRITICAL:
			self.setIcon(self.Critical)
		
		self.exec_()

	def showMessageWithText(self, message_text):
		self.setText(message_text)
		self.setIcon(self.Information)
		self.exec_()