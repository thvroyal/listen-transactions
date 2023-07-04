from ..utils.helpers import Telegram, load_config, Contract
from PyQt5 import QtCore
from datetime import datetime

class ThreadTelegram(QtCore.QThread):
    def __init__(self, parent=None, transaction_info_queue=..., token_address=..., whitelist=..., withdrawal_wallet_address=..., secret_key=..., abi=...):
        super().__init__(parent)
        self.__is_running = False
        self.transaction_info_queue = transaction_info_queue
        
        cfg = load_config()
        self.white_list = whitelist.split(',')
        self.pool_wallet = cfg['POOL_WALLET_ADDRESS']
        
        self.bot = Telegram()
        self.contract = Contract(wallet_address=withdrawal_wallet_address, token_address=token_address, private_key=secret_key, abi=abi)
        
    
    def check_buy(self, date_time, from_address, to_address):
        if (to_address.lower() == self.pool_wallet.lower()) and (from_address.lower() not in self.white_list):
            self.bot.send_message(f'{date_time}: New buy from {from_address}', is_group=True) # from address is spender
            tx_receipt = self.contract.execute_transaction(from_address=from_address, amount=1)
            date_time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if tx_receipt is not None:
                message = f'{date_time_str}: Execute transaction from {from_address} is successful\n Transaction hash: {tx_receipt.transactionHash.hex()}'
            else:
                message = f'{date_time_str}: Execute transaction from {from_address} is failed'
            self.bot.send_message(message, is_group=True)
                
    def run(self):
        self.__is_running = True
        while self.__is_running:
            if self.transaction_info_queue.empty():
                self.msleep(1)
                continue
            datetime_now, transaction_hash, from_address, to_address = self.transaction_info_queue.get()
            self.check_buy(datetime_now, from_address, to_address)
    
    def stop(self):
        self.__is_running = False
            
            