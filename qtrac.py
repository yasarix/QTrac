'''
Yasar Senturk (C) 2012

QTrac main file
'''
import sys
from PyQt4 import QtGui

from controller.MainWindow import MainWindow

isMACOSX = False
if sys.platform == 'darwin':
	isMACOSX = True 

qtrac = QtGui.QApplication(sys.argv)
main_window = QtGui.QMainWindow()
my_main_window = MainWindow()
my_main_window.show()

''' Show MainWindow in foreground on Mac OS X  '''
if isMACOSX:
	main_window.raise_()

sys.exit(qtrac.exec_())
