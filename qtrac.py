'''
Yasar Senturk (C) 2012

QTrac main file
'''
import sys
from PyQt4 import QtGui
import config
from Trac.TracServer import *
from Trac.Ticket import *

from controller.MainWindow import MainWindow

isMACOSX = hasattr(QtGui, "qt_mac_set_native_menubar")

qtrac = QtGui.QApplication(sys.argv)
main_window = QtGui.QMainWindow()
my_main_window = MainWindow()
my_main_window.show()

sys.exit(qtrac.exec_())

'''my_trac = TracServer(config.server_url, config.username, config.password)
ticket = Ticket(my_trac)
ticket.listTickets("")
'''