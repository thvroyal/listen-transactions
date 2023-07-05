from ..layouts.main_window import Ui_MainWindow
from PyQt5 import QtWidgets
from ...threads import ThreadIntegrateApi, ThreadTelegram
from queue import Queue
import pandas as pd
from ...objects.transaction import Transaction
from typing import List
from ...utils.helpers import load_config


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_stop.setEnabled(False)
        
        self.transactions_info = pd.DataFrame(columns=['datetime', 'transaction_hash', 'maker'])
        
        self.load_from_config()
        self.create_queues()
        self.connect_button_signals()
    
    def load_from_config(self):
        try:
            cfg = load_config()
        except:
            return
        token_address = cfg['TOKEN_ADDRESS']
        pair_address = cfg['PAIR_ADDRESS']
        whitelist = cfg['WHITELIST']
        withdrawal_wallet_address = cfg['WITHDRAWAL_WALLET_ADDRESS']
        withdrawal_wallet_secret_key = cfg['WITHDRAWAL_WALLET_SECRET_KEY']
        contract_abi = cfg['CONTRACT_ABI']
                
        self.ui.qline_token_address.setText(token_address)
        self.ui.qline_pair_address.setText(pair_address)
        self.ui.qline_whitelist.setText(whitelist)
        
        self.ui.qline_withdrawal_wallet_address.setText(withdrawal_wallet_address)
        self.ui.qline_withdrawal_wallet_secret_key.setText(withdrawal_wallet_secret_key)
        self.ui.qline_contract_abi.setText(contract_abi)
    
    def connect_button_signals(self):
        self.ui.btn_start.clicked.connect(self.start)
        self.ui.btn_stop.clicked.connect(self.stop)
    
    def connect_emit_signals(self):
        self.thread_integrate_api.sig_new_transaction.connect(self.update_transactions_info)
        
    def create_queues(self):
        self.transaction_queue = Queue()
        self.transaction_info_queue = Queue()
        
    def create_threads(self):
        self.thread_integrate_api = ThreadIntegrateApi(parent=self, pair=self.ui.qline_pair_address.text(), transaction_queue=self.transaction_queue)
        self.thread_telegram = ThreadTelegram(parent=self, transaction_queue=self.transaction_queue, token_address=self.ui.qline_token_address.text(),whitelist=self.ui.qline_whitelist.text(), withdrawal_wallet_address=self.ui.qline_withdrawal_wallet_address.text(), secret_key=self.ui.qline_withdrawal_wallet_secret_key.text(), abi=self.ui.qline_contract_abi.text())
        
        self.list_threads = [self.thread_integrate_api, self.thread_telegram]
        
    def start_all_threads(self):
        for thread in self.list_threads:
            thread.start()
            
    def stop_all_threads(self):
        for thread in self.list_threads:
            thread.stop()
        self.list_threads = []
    
    def update_transactions_info(self, new_transaction: List[Transaction]):
        for transaction in new_transaction:
            transaction_df = pd.DataFrame([[transaction.date_time, transaction.blockHash, transaction.maker]], columns=['datetime', 'block_hash', 'maker'])
            self.transactions_info = pd.concat([self.transactions_info, transaction_df], ignore_index=True)
        self.ui.tableWidget.setRowCount(self.transactions_info.shape[0])
        self.ui.tableWidget.setColumnCount(self.transactions_info.shape[1])
        self.ui.tableWidget.setHorizontalHeaderLabels(self.transactions_info.columns)
        for row in range(self.transactions_info.shape[0]):
            for col in range(self.transactions_info.shape[1]):
                item = QtWidgets.QTableWidgetItem(str(self.transactions_info.iloc[row, col]))
                self.ui.tableWidget.setItem(row, col, item)
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.show()
        
    def set_state_qline(self, enable=False):
        self.ui.qline_token_address.setEnabled(enable)
        self.ui.qline_whitelist.setEnabled(enable)
        self.ui.qline_withdrawal_wallet_address.setEnabled(enable)
        self.ui.qline_withdrawal_wallet_secret_key.setEnabled(enable)
        self.ui.qline_contract_abi.setEnabled(enable)
        
    def start(self):
        if not self.ui.qline_token_address.text():
            QtWidgets.QMessageBox.warning(self, "Warning", "Please enter token address")
            return
        if not self.ui.qline_withdrawal_wallet_address.text():
            QtWidgets.QMessageBox.warning(self, "Warning", "Please enter withdrawal wallet address")
            return
        if not self.ui.qline_withdrawal_wallet_secret_key.text():
            QtWidgets.QMessageBox.warning(self, "Warning", "Please enter withdrawal wallet secret key")
            return
        if not self.ui.qline_contract_abi.text():
            QtWidgets.QMessageBox.warning(self, "Warning", "Please enter contract abi")
            return
        
        self.create_threads()
        self.connect_emit_signals()
        self.start_all_threads()
        self.ui.btn_start.setEnabled(False)
        self.ui.btn_stop.setEnabled(True)
        self.set_state_qline(False)
        
    def stop(self):
        self.stop_all_threads()
        self.ui.btn_start.setEnabled(True)
        self.ui.btn_stop.setEnabled(False)
        self.set_state_qline(True)
        
        
        
        
    