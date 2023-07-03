from ..utils.helpers import Telegram, load_config
from PyQt5 import QtCore


class ThreadTelegram(QtCore.QThread):
    def __init__(self, parent=None, main_wallet=..., transaction_info_queue=...):
        super().__init__(parent)
        self.__is_running = False
        self.transaction_info_queue = transaction_info_queue
        self.main_wallet = main_wallet
        
        cfg = load_config()
        self.white_list = cfg['WHITE_LIST']
        
        self.bot = Telegram()
        
    @staticmethod
    def do_something():    
        pass
    
    def check_buy(self, date_time, from_address, to_address):
        if to_address.lower() == self.main_wallet.lower():
            self.bot.send_message(f'New buy from {from_address} at {date_time}', is_group=True)
            if to_address.lower() in self.white_list:
                self.do_something()
    
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
            
            