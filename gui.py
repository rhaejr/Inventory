# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.main_label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_label.sizePolicy().hasHeightForWidth())
        self.main_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.main_label.setFont(font)
        self.main_label.setObjectName(_fromUtf8("main_label"))
        self.horizontalLayout_3.addWidget(self.main_label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_7.addWidget(self.label_7)
        self.search_edit = QtGui.QLineEdit(self.tab_2)
        self.search_edit.setObjectName(_fromUtf8("search_edit"))
        self.verticalLayout_7.addWidget(self.search_edit)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        r
        self.ipc_button = QtGui.QPushButton(self.tab_2)
        self.ipc_button.setObjectName(_fromUtf8("ipc_button"))
        self.horizontalLayout.addWidget(self.ipc_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_8.addWidget(self.label_8)
        self.nsn_edit = QtGui.QLineEdit(self.tab)
        self.nsn_edit.setObjectName(_fromUtf8("nsn_edit"))
        self.verticalLayout_8.addWidget(self.nsn_edit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_9.addWidget(self.label_9)
        self.pn_edit = QtGui.QLineEdit(self.tab)
        self.pn_edit.setObjectName(_fromUtf8("pn_edit"))
        self.verticalLayout_9.addWidget(self.pn_edit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_10.addWidget(self.label_10)
        self.desc_edit = QtGui.QLineEdit(self.tab)
        self.desc_edit.setObjectName(_fromUtf8("desc_edit"))
        self.verticalLayout_10.addWidget(self.desc_edit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_11.addWidget(self.label_11)
        self.loc_edit = QtGui.QLineEdit(self.tab)
        self.loc_edit.setObjectName(_fromUtf8("loc_edit"))
        self.verticalLayout_11.addWidget(self.loc_edit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.label_12 = QtGui.QLabel(self.tab)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_12.addWidget(self.label_12)
        self.niin_edit = QtGui.QLineEdit(self.tab)
        self.niin_edit.setObjectName(_fromUtf8("niin_edit"))
        self.verticalLayout_12.addWidget(self.niin_edit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.label_13 = QtGui.QLabel(self.tab)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_13.addWidget(self.label_13)
        self.remarks_edit = QtGui.QLineEdit(self.tab)
        self.remarks_edit.setObjectName(_fromUtf8("remarks_edit"))
        self.verticalLayout_13.addWidget(self.remarks_edit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.update_button = QtGui.QPushButton(self.tab)
        self.update_button.setObjectName(_fromUtf8("update_button"))
        self.verticalLayout_14.addWidget(self.update_button)
        self.add_button = QtGui.QPushButton(self.tab)
        self.add_button.setObjectName(_fromUtf8("add_button"))
        self.verticalLayout_14.addWidget(self.add_button)
        self.horizontalLayout_2.addLayout(self.verticalLayout_14)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.add_label_btn = QtGui.QPushButton(self.tab_3)
        self.add_label_btn.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.add_label_btn.setObjectName(_fromUtf8("add_label_btn"))
        self.print_label_btn = QtGui.QPushButton(self.tab_3)
        self.print_label_btn.setGeometry(QtCore.QRect(120, 10, 93, 28))
        self.print_label_btn.setObjectName(_fromUtf8("print_label_btn"))
        self.reset_labels_btn = QtGui.QPushButton(self.tab_3)
        self.reset_labels_btn.setGeometry(QtCore.QRect(230, 10, 93, 28))
        self.reset_labels_btn.setObjectName(_fromUtf8("reset_labels_btn"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.reset_table_button = QtGui.QPushButton(self.centralwidget)
        self.reset_table_button.setObjectName(_fromUtf8("reset_table_button"))
        self.verticalLayout.addWidget(self.reset_table_button)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMain = QtGui.QMenu(self.menubar)
        self.menuMain.setObjectName(_fromUtf8("menuMain"))
        MainWindow.setMenuBar(self.menubar)
        self.actionLUH = QtGui.QAction(MainWindow)
        self.actionLUH.setObjectName(_fromUtf8("actionLUH"))
        self.actionApache = QtGui.QAction(MainWindow)
        self.actionApache.setObjectName(_fromUtf8("actionApache"))
        self.menuMain.addAction(self.actionLUH)
        self.menuMain.addAction(self.actionApache)
        self.menubar.addAction(self.menuMain.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Benchstock", None))
        self.main_label.setText(_translate("MainWindow", "Apache", None))
        self.label_7.setText(_translate("MainWindow", "Search", None))
        self.search_button.setText(_translate("MainWindow", "Search", None))
        self.ipc_button.setText(_translate("MainWindow", "IPC", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Search", None))
        self.label_8.setText(_translate("MainWindow", "NSN", None))
        self.label_9.setText(_translate("MainWindow", "PN", None))
        self.label_10.setText(_translate("MainWindow", "Description", None))
        self.label_11.setText(_translate("MainWindow", "Location", None))
        self.label_12.setText(_translate("MainWindow", "NIIN", None))
        self.label_13.setText(_translate("MainWindow", "Remarks", None))
        self.update_button.setText(_translate("MainWindow", "Update", None))
        self.add_button.setText(_translate("MainWindow", "Add", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Edit", None))
        self.add_label_btn.setText(_translate("MainWindow", "Add Label", None))
        self.print_label_btn.setText(_translate("MainWindow", "Print Labels", None))
        self.reset_labels_btn.setText(_translate("MainWindow", "Reset Labels", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Labels", None))
        self.reset_table_button.setText(_translate("MainWindow", "Reset Table", None))
        self.menuMain.setTitle(_translate("MainWindow", "Aircraft", None))
        self.actionLUH.setText(_translate("MainWindow", "LUH", None))
        self.actionApache.setText(_translate("MainWindow", "Apache", None))

