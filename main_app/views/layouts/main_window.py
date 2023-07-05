# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/layouts/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1105, 779)
        MainWindow.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setStyleSheet("border: none;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_3.setAutoFillBackground(False)
        self.groupBox_3.setStyleSheet("border: none;")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.btn_start = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_start.setGeometry(QtCore.QRect(10, 30, 191, 50))
        self.btn_start.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_start.setStyleSheet("QPushButton {\n"
"    border-radius: 8px;    \n"
"    color: rgba(255, 255, 255, .7);\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"    background-color: rgb(85, 85, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #6a6aff;\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color:#4848fa;\n"
"}\n"
"QPushButton:disabled {\n"
"        background-color: rgba(85, 85, 255, .1);\n"
"}")
        self.btn_start.setObjectName("btn_start")
        self.btn_stop = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_stop.setGeometry(QtCore.QRect(10, 110, 191, 50))
        self.btn_stop.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_stop.setStyleSheet("QPushButton {\n"
"    border-radius: 8px;    \n"
"    color: rgba(255, 255, 255, .7);\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"    background-color: rgba(255, 47, 50, .8);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 47, 50, 1);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(255, 47, 50, .6);\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: rgba(255, 47, 50, .1);\n"
"}")
        self.btn_stop.setObjectName("btn_stop")
        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setStyleSheet("border: none;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setStyleSheet("color: rgba(255, 255, 255, 0.6);")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 10, 0, 1, 1)
        self.qline_contract_abi = QtWidgets.QLineEdit(self.groupBox)
        self.qline_contract_abi.setMinimumSize(QtCore.QSize(0, 30))
        self.qline_contract_abi.setStyleSheet("QLineEdit {\n"
"    background-color: rgba(255, 255, 255, .1);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.qline_contract_abi.setPlaceholderText("")
        self.qline_contract_abi.setObjectName("qline_contract_abi")
        self.gridLayout_2.addWidget(self.qline_contract_abi, 11, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setStyleSheet("color: rgba(255, 255, 255, 0.6);")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.qline_withdrawal_wallet_address = QtWidgets.QLineEdit(self.groupBox)
        self.qline_withdrawal_wallet_address.setMinimumSize(QtCore.QSize(0, 30))
        self.qline_withdrawal_wallet_address.setStyleSheet("QLineEdit {\n"
"    background-color: rgba(255, 255, 255, .1);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.qline_withdrawal_wallet_address.setPlaceholderText("")
        self.qline_withdrawal_wallet_address.setObjectName("qline_withdrawal_wallet_address")
        self.gridLayout_2.addWidget(self.qline_withdrawal_wallet_address, 7, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setStyleSheet("color: rgba(255, 255, 255, 0.6);")
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 8, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setStyleSheet("color: rgba(255, 255, 255, 0.6);\n"
"margin-top: 24px;")
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 6, 0, 1, 1)
        self.qline_token_address = QtWidgets.QLineEdit(self.groupBox)
        self.qline_token_address.setMinimumSize(QtCore.QSize(0, 30))
        self.qline_token_address.setStyleSheet("QLineEdit {\n"
"    background-color: rgba(255, 255, 255, .1);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.qline_token_address.setPlaceholderText("")
        self.qline_token_address.setObjectName("qline_token_address")
        self.gridLayout_2.addWidget(self.qline_token_address, 1, 0, 1, 1)
        self.qline_whitelist = QtWidgets.QLineEdit(self.groupBox)
        self.qline_whitelist.setMinimumSize(QtCore.QSize(0, 30))
        self.qline_whitelist.setStyleSheet("QLineEdit {\n"
"    background-color: rgba(255, 255, 255, .1);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.qline_whitelist.setPlaceholderText("")
        self.qline_whitelist.setObjectName("qline_whitelist")
        self.gridLayout_2.addWidget(self.qline_whitelist, 5, 0, 1, 1)
        self.qline_withdrawal_wallet_secret_key = QtWidgets.QLineEdit(self.groupBox)
        self.qline_withdrawal_wallet_secret_key.setMinimumSize(QtCore.QSize(0, 30))
        self.qline_withdrawal_wallet_secret_key.setStyleSheet("QLineEdit {\n"
"    background-color: rgba(255, 255, 255, .1);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.qline_withdrawal_wallet_secret_key.setPlaceholderText("")
        self.qline_withdrawal_wallet_secret_key.setObjectName("qline_withdrawal_wallet_secret_key")
        self.gridLayout_2.addWidget(self.qline_withdrawal_wallet_secret_key, 9, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setStyleSheet("color: rgba(255, 255, 255, 0.6);")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.qline_pair_address = QtWidgets.QLineEdit(self.groupBox)
        self.qline_pair_address.setMinimumSize(QtCore.QSize(0, 30))
        self.qline_pair_address.setStyleSheet("QLineEdit {\n"
"    background-color: rgba(255, 255, 255, .1);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.qline_pair_address.setPlaceholderText("")
        self.qline_pair_address.setObjectName("qline_pair_address")
        self.gridLayout_2.addWidget(self.qline_pair_address, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setStyleSheet("color: rgba(255, 255, 255, 0.6);")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setStyleSheet("border: none;\n"
"border-radius: 8px;\n"
"background: rgb(255, 255, 255);\n"
"color: black;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_3.addWidget(self.tableWidget, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setStyleSheet("color: rgba(255, 255, 255, .7);\n"
"font-size: 16px;")
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1105, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.btn_stop.setText(_translate("MainWindow", "Stop"))
        self.label_9.setText(_translate("MainWindow", "Contract ABI"))
        self.label_5.setText(_translate("MainWindow", "Whitelist"))
        self.label_8.setText(_translate("MainWindow", "Withdrawal Wallet Secret Key"))
        self.label_6.setText(_translate("MainWindow", "Withdrawal Wallet Address"))
        self.label_3.setText(_translate("MainWindow", "Token Address "))
        self.label_4.setText(_translate("MainWindow", "Pair Address "))
        self.label_10.setText(_translate("MainWindow", "History Transaction"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
