from PyQt5 import QtCore
from collections import deque
import time
from ..services.integrate_dextools_api import api_get_token_info
from ..objects.transaction import Transaction


class ThreadIntegrateApi(QtCore.QThread):
    sig_new_transaction = QtCore.pyqtSignal(list)
    
    def __init__(self, parent=None, pair=..., transaction_queue=...):
        super().__init__(parent)
        self.__is_running = False
        self.transaction_queue = transaction_queue
        
        self.pair = pair.lower()
        
        self.old_transaction_id = deque(maxlen=100)
        
    def run(self):
        self.__is_running = True
        print("Thread Integrate started")
        old_time = time.time()
        old_max_timestamp = time.time()
        while self.__is_running:
            if time.time() - old_time < 1:
                self.msleep(1)
                continue
            new_transactions = []
            old_time = time.time()
            token_info = api_get_token_info(self.pair)
            if token_info is None:
                continue
            try:
                all_transactions = token_info['data']['swaps']
            except:
                continue
            for transaction_dict in all_transactions:
                transaction = Transaction(transaction_dict)
                if transaction.timestamp < old_max_timestamp:
                    continue
                if transaction.id in self.old_transaction_id:
                    continue
                new_transactions.append(transaction)
                self.old_transaction_id.append(transaction.id)
            if len(new_transactions) > 0:
                old_max_timestamp = max([transaction.timestamp for transaction in new_transactions])
                self.transaction_queue.put(new_transactions)
                self.sig_new_transaction.emit(new_transactions)
                
    def stop(self):
        print("Stopped Thread Socket")
        self.__is_running = False