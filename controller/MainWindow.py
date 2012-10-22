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
		
		'''Ticket List Model'''
		ticket_list = QtGui.QStandardItemModel(0, 7)
		ticket_list.setHeaderData(0, QtCore.Qt.Horizontal , QtCore.QVariant("Ticket Number"))
		ticket_list.setHeaderData(1, QtCore.Qt.Horizontal , QtCore.QVariant("Creation Date"))
		ticket_list.setHeaderData(2, QtCore.Qt.Horizontal , QtCore.QVariant("Milestone"))
		ticket_list.setHeaderData(3, QtCore.Qt.Horizontal , QtCore.QVariant("Summary"))
		ticket_list.setHeaderData(4, QtCore.Qt.Horizontal , QtCore.QVariant("Type"))
		ticket_list.setHeaderData(5, QtCore.Qt.Horizontal , QtCore.QVariant("Owner"))
		ticket_list.setHeaderData(6, QtCore.Qt.Horizontal , QtCore.QVariant("Status"))
		
		'''
		ticket_list.insertRow(0)
		'''
		
		self.ui.ticketListTree.setModel(ticket_list)
		parent_item = ticket_list.invisibleRootItem()
		root_item = QtGui.QStandardItem(QtCore.QString("My Tickets"))
		parent_item.appendRow(root_item)
		parent_item = root_item

		parent_item.appendRow(
							[
								QtGui.QStandardItem(QtCore.QString("1")),
								QtGui.QStandardItem(QtCore.QString("2012-10-21")),
								QtGui.QStandardItem(QtCore.QString("Deneme")),
								QtGui.QStandardItem(QtCore.QString("Bu bir denemedir")),
								QtGui.QStandardItem(QtCore.QString("bug")),
								QtGui.QStandardItem(QtCore.QString("yasar")),
								QtGui.QStandardItem(QtCore.QString("new"))
							])

		root_item = QtGui.QStandardItem(QtCore.QString("Tickets that I follow"))
		parent_item = ticket_list.invisibleRootItem()
		parent_item.appendRow(root_item)
		parent_item = root_item

		parent_item.appendRow(
							[
								QtGui.QStandardItem(QtCore.QString("1")),
								QtGui.QStandardItem(QtCore.QString("2012-10-21")),
								QtGui.QStandardItem(QtCore.QString("Deneme")),
								QtGui.QStandardItem(QtCore.QString("Bu bir denemedir")),
								QtGui.QStandardItem(QtCore.QString("bug")),
								QtGui.QStandardItem(QtCore.QString("yasar")),
								QtGui.QStandardItem(QtCore.QString("new"))
							])

	
	def refreshTicketList(self):
		self.ui.statusbar.showMessage("Refreshing")
		
	def modifyTicketQuery(self):
		self.ui.statusbar.showMessage("Modifying query")
