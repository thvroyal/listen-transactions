import json
from PyQt5 import QtCore
from collections import deque
import time
from ..services.integrate_dextools_api import api_get_token_info
from ..objects.transaction import Transaction
from ..utils.helpers import SeleniumChrome


class ThreadIntegrateApi(QtCore.QThread):
    sig_new_transaction = QtCore.pyqtSignal(list)

    def __init__(self, parent=None, pair=..., transaction_queue=..., selenium_chrome: SeleniumChrome = ...):
        super().__init__(parent)
        self.__is_running = False
        self.transaction_queue = transaction_queue

        self.selenium_chrome = selenium_chrome

        self.pair = pair.lower()
        print(f"Pair: {self.pair}")

        self.is_call_transaction = False
        self.old_transaction_id = deque(maxlen=100)

    def change_call_transaction_state(self, state):
        self.is_call_transaction = state

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
            token_info = api_get_token_info(self.selenium_chrome, self.pair)
            if token_info is None:
                continue
            try:
                all_transactions = token_info['data']['swaps']
            except Exception as e:
                print("Exception when get all transactions: ", e)
                continue
            for transaction_dict in all_transactions:
                transaction = Transaction()
                transaction.load_from_dict(transaction_dict)
                if transaction.timestamp < old_max_timestamp:
                    continue
                if transaction.id in self.old_transaction_id:
                    continue
                print(f"New transaction: {transaction}")
                new_transactions.append(transaction)
                self.old_transaction_id.append(transaction.id)

            if len(new_transactions) > 0:
                old_max_timestamp = max(
                    [transaction.timestamp for transaction in new_transactions])
                if self.is_call_transaction:
                    self.transaction_queue.put(new_transactions)
                print(f"New transactions: {len(new_transactions)}")
                self.sig_new_transaction.emit(new_transactions)

    def stop(self):
        print("Stopped Thread Socket")
        self.__is_running = False
