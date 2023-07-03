from ..utils.helpers import load_config
from web3 import Web3
from PyQt5 import QtCore
import yaml


class ThreadTransactionInfo(QtCore.QThread):
    sig_transaction_info = QtCore.pyqtSignal(list)
    
    def __init__(self, parent=None, transaction_queue=..., transaction_info_queue=...):
        super().__init__(parent)
        self.__is_running = False
        self.transaction_queue = transaction_queue
        self.transaction_info_queue = transaction_info_queue
        
        cfg = load_config()
        nodeHttpsUrl = cfg['INFURA_MAINNET_HTTPS_URL'] + cfg['INFURA_PROJECT_ID']
        self.web3 = Web3(Web3.HTTPProvider(nodeHttpsUrl))
    
    def get_transaction_info(self, transaction_hash):
        return self.web3.eth.get_transaction(transaction_hash)
    
    def run(self):
        self.__is_running = True
        while self.__is_running:
            if self.transaction_queue.empty():
                self.msleep(1)
                continue
            datetime_now, transaction_hash = self.transaction_queue.get()
            try:
                transaction_info = self.get_transaction_info(transaction_hash)
            except Exception as e:
                print(e)
                continue
            from_address = transaction_info['from']
            to_address = transaction_info['to']
            print(datetime_now, transaction_hash, from_address, to_address)
            self.sig_transaction_info.emit([datetime_now, transaction_hash, from_address, to_address])
            self.transaction_info_queue.put([datetime_now, transaction_hash, from_address, to_address])
    
    def stop(self):
        self.__is_running = False
            
            