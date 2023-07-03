from ..layouts.main_window import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from ...threads import ThreadSocket, ThreadTransactionInfo
from queue import Queue
import pandas as pd


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.transactions_info = pd.DataFrame(columns=['datetime', 'transaction_hash', 'from_address', 'to_address'])
        
        self.create_queues()
        self.connect_button_signals()
    
    def connect_button_signals(self):
        self.ui.btn_start.clicked.connect(self.start)
    
    def connect_emit_signals(self):
        self.thread_transaction_info.sig_transaction_info.connect(self.update_transactions_info)
        
    def create_queues(self):
        self.transaction_queue = Queue()
        
    def create_threads(self):
        self.thread_socket = ThreadSocket(parent=self, token=self.ui.qline_token.text(), transaction_queue=self.transaction_queue)
        self.thread_transaction_info = ThreadTransactionInfo(parent=self, transaction_queue=self.transaction_queue)
        
        self.list_threads = [self.thread_socket, self.thread_transaction_info]
        
    def start_all_threads(self):
        for thread in self.list_threads:
            thread.start()
    
    def update_transactions_info(self, transaction_info):
        datetime_now, transaction_hash, from_address, to_address = transaction_info
        transaction_df = pd.DataFrame([[datetime_now, transaction_hash, from_address, to_address]], columns=['datetime', 'transaction_hash', 'from_address', 'to_address'])
        self.transactions_info = pd.concat([self.transactions_info, transaction_df], ignore_index=True)
        self.ui.tableWidget.setRowCount(self.transactions_info.shape[0])
        self.ui.tableWidget.setColumnCount(self.transactions_info.shape[1])
        self.ui.tableWidget.setHorizontalHeaderLabels(self.transactions_info.columns)
        for row in range(self.transactions_info.shape[0]):
            for col in range(self.transactions_info.shape[1]):
                item = QtWidgets.QTableWidgetItem(str(self.transactions_info.iloc[row, col]))
                self.ui.tableWidget.setItem(row, col, item)
        self.ui.tableWidget.show()
        
    def start(self):
        if not self.ui.qline_project_id.text():
            QtWidgets.QMessageBox.warning(self, "Warning", "Please enter project id")
            return
        if not self.ui.qline_token.text():
            QtWidgets.QMessageBox.warning(self, "Warning", "Please enter token")
            return
        if not self.ui.qline_main_wallet.text():
            QtWidgets.QMessageBox.warning(self, "Warning", "Please enter main wallet")
            return
        self.create_threads()
        self.connect_emit_signals()
        self.start_all_threads()
        
        
        
        
    