from PyQt4 import QtCore
from PyQt4 import QtGui
from ui.MainWindow import Ui_MainWindow

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
		''' Signals '''
		#self.ui.pushButton.clicked.connect(self.PushButtonClicked)
		QtCore.QObject.connect(self.ui.actionRefreshTicketList, QtCore.SIGNAL(_fromUtf8("triggered()")), self.refreshTicketList)
		QtCore.QObject.connect(self.ui.actionTicketQuery, QtCore.SIGNAL(_fromUtf8("triggered()")), self.modifyTicketQuery)
	
	def refreshTicketList(self):
		self.ui.statusbar.showMessage("Refreshing")
		
	def modifyTicketQuery(self):
		self.ui.statusbar.showMessage("Modifying query")
