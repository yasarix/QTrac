# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Sun Nov  4 03:39:16 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(914, 589)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ticketListTree = QtGui.QTreeView(self.centralwidget)
        self.ticketListTree.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ticketListTree.setTabKeyNavigation(True)
        self.ticketListTree.setAlternatingRowColors(True)
        self.ticketListTree.setObjectName(_fromUtf8("ticketListTree"))
        self.verticalLayout.addWidget(self.ticketListTree)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 914, 22))
        self.menubar.setDefaultUp(True)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionRefreshTicketList = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("resources/view-refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefreshTicketList.setIcon(icon)
        self.actionRefreshTicketList.setObjectName(_fromUtf8("actionRefreshTicketList"))
        self.actionAddQuery = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("resources/edit-add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddQuery.setIcon(icon1)
        self.actionAddQuery.setObjectName(_fromUtf8("actionAddQuery"))
        self.actionModifyQuery = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("resources/edit-6.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionModifyQuery.setIcon(icon2)
        self.actionModifyQuery.setObjectName(_fromUtf8("actionModifyQuery"))
        self.actionDeleteQuery = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("resources/edit-remove-3.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeleteQuery.setIcon(icon3)
        self.actionDeleteQuery.setObjectName(_fromUtf8("actionDeleteQuery"))
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.actionRefreshTicketList)
        self.toolBar.addAction(self.actionAddQuery)
        self.toolBar.addAction(self.actionModifyQuery)
        self.toolBar.addAction(self.actionDeleteQuery)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "QTrac", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefreshTicketList.setText(QtGui.QApplication.translate("MainWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefreshTicketList.setToolTip(QtGui.QApplication.translate("MainWindow", "Refresh ticket list from server", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefreshTicketList.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddQuery.setText(QtGui.QApplication.translate("MainWindow", "Add Query", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddQuery.setToolTip(QtGui.QApplication.translate("MainWindow", "Add a custom query", None, QtGui.QApplication.UnicodeUTF8))
        self.actionModifyQuery.setText(QtGui.QApplication.translate("MainWindow", "Modify Query", None, QtGui.QApplication.UnicodeUTF8))
        self.actionModifyQuery.setToolTip(QtGui.QApplication.translate("MainWindow", "Modify selected custome query", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteQuery.setText(QtGui.QApplication.translate("MainWindow", "Delete Query", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteQuery.setToolTip(QtGui.QApplication.translate("MainWindow", "Delete selected custome query. Your tickets on server will not be deleted.", None, QtGui.QApplication.UnicodeUTF8))

