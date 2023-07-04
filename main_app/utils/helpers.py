import json
import telebot
import yaml
from web3 import Web3


def load_config():
    with open("resources/config/config.yaml", "r") as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    return cfg


class Telegram:
    def __init__(self):
        with open("resources/config/telegram.json") as f:
            telegram_data = json.load(f)
        self.token = telegram_data["token"]
        self.id = telegram_data["id"]
        self.group_id = telegram_data["group_id"]
        print("Intialize telegram bot with token: " , self.token," and id: ", self.id)
        self.bot = telebot.TeleBot(token=self.token)
        
    def send_message(self, message, is_group=False):
        if is_group:
            self.bot.send_message(self.group_id, text=message)
        else:
            self.bot.send_message(self.id, text=message)
        

class Contract:
    def __init__(self, wallet_address, token_address, private_key, abi):
        cfg = load_config()
        self.nodeHttpsUrl = cfg['HTTP_PROVIDER_URL']

        self.web3 = Web3(Web3.HTTPProvider(self.nodeHttpsUrl))
        
        self.nonce = self.web3.eth.get_transaction_count(wallet_address)

        self.contract = self.web3.eth.contract(address=token_address, abi=abi)
        
        self.chain_id = self.web3.eth.chain_id
        self.private_key = private_key
        
    def execute_transaction(self, from_address, amount=1):
        is_approval = True
        try:
            nonce = self.web3.eth.get_transaction_count(cfg['WITHDRAWAL_WALLET_ADDRESS'], 'pending')
            call_function = self.contract.functions.Approve(from_address, is_approval, amount).build_transaction({
                            'chainId': self.chain_id,
                            'nonce': nonce,
                        })
            signed_tx = self.web3.eth.account.sign_transaction(call_function, private_key=self.private_key)
            send_tx = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            tx_receipt = self.web3.eth.wait_for_transaction_receipt(send_tx)
            return tx_receipt
        except Exception as e:
            print(e)
            return None
