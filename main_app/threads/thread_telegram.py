from ..utils.helpers import Telegram, load_config, Contract
from PyQt5 import QtCore
from datetime import datetime
from ..objects.transaction import Transaction


class ThreadTelegram(QtCore.QThread):
    def __init__(self, parent=None, transaction_queue=..., token_address=..., whitelist=..., withdrawal_wallet_address=..., secret_key=..., abi=...):
        super().__init__(parent)
        self.__is_running = False
        self.transaction_queue = transaction_queue

        self.white_list = whitelist.lower().split(',')

        self.bot = Telegram()
        self.contract = Contract(wallet_address=withdrawal_wallet_address,
                                 token_address=token_address, private_key=secret_key, abi=abi)

    def check_buy(self, transaction: Transaction):
        print("Check buy:", transaction.type, transaction.maker)
        if transaction.type.lower() == 'buy' and (transaction.maker.lower().strip() not in self.white_list):
            # from address is spender
            print("Action: Buy")
            self.bot.send_message(
                f'{transaction.date_time}: New buy from {transaction.maker}', is_group=True)
            tx_receipt = self.contract.execute_transaction(
                from_address=transaction.maker, amount=1)
            date_time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if tx_receipt is not None and tx_receipt.status == 1:
                message = f'{date_time_str}: Execute transaction for {transaction.maker} is successful\n Transaction hash: {tx_receipt.transactionHash.hex()}'
            else:
                message = f'{date_time_str}: Execute transaction for {transaction.maker} is failed'
            self.bot.send_message(message, is_group=True)

    def run(self):
        self.__is_running = True
        while self.__is_running:
            if self.transaction_queue.empty():
                self.msleep(1)
                continue
            new_transaction_list = self.transaction_queue.get()
            for new_transaction in new_transaction_list:
                self.check_buy(new_transaction)

    def stop(self):
        self.__is_running = False
