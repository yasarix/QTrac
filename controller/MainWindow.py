from PyQt4 import QtCore
from PyQt4 import QtGui
from ui.MainWindow import Ui_MainWindow
import config
from Trac.TracServer import *
from Trac.Ticket import *

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
		
		self.refreshTicketList()
	
	def refreshTicketList(self):
		self.ui.statusbar.showMessage(_fromUtf8("Fetching list of tickets from server"))

		my_trac = TracServer(config.server_url, config.username, config.password)
		ticket = Ticket(my_trac)
		found_tickets = ticket.listTickets("")
		
		print found_tickets
		print "\n"

		'''Ticket List Model'''
		ticket_model = QtGui.QStandardItemModel(0, 7)
		ticket_model.setHeaderData(0, QtCore.Qt.Horizontal, QtCore.QVariant("Ticket Number"))
		ticket_model.setHeaderData(1, QtCore.Qt.Horizontal, QtCore.QVariant("Creation Date"))
		ticket_model.setHeaderData(2, QtCore.Qt.Horizontal, QtCore.QVariant("Milestone"))
		ticket_model.setHeaderData(3, QtCore.Qt.Horizontal, QtCore.QVariant("Summary"))
		ticket_model.setHeaderData(4, QtCore.Qt.Horizontal, QtCore.QVariant("Type"))
		ticket_model.setHeaderData(5, QtCore.Qt.Horizontal, QtCore.QVariant("Owner"))
		ticket_model.setHeaderData(6, QtCore.Qt.Horizontal, QtCore.QVariant("Status"))
		
		'''
		ticket_model.insertRow(0)
		'''
		
		self.ui.ticketListTree.setModel(ticket_model)
		parent_item = ticket_model.invisibleRootItem()
		root_item = QtGui.QStandardItem(QtCore.QString("My Tickets"))
		parent_item.appendRow(root_item)
		parent_item = root_item

		for ticket in found_tickets:
			parent_item.appendRow(
					[
						QtGui.QStandardItem(QtCore.QString(str(ticket[0]))),
						QtGui.QStandardItem(QtCore.QString(str(ticket[3]['time']))),
						QtGui.QStandardItem(QtCore.QString(str(ticket[3]['milestone']))),
						QtGui.QStandardItem(QtCore.QString(str(ticket[3]['summary']))),
						QtGui.QStandardItem(QtCore.QString(str(ticket[3]['type']))),
						QtGui.QStandardItem(QtCore.QString(str(ticket[3]['owner']))),
						QtGui.QStandardItem(QtCore.QString(str(ticket[3]['status'])))
					])

	def modifyTicketQuery(self):
		self.ui.statusbar.showMessage("Modifying query")
