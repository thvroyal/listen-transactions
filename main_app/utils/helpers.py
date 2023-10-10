import json
import telebot
import yaml
from web3 import Web3
from datetime import datetime
import pytz
import os
import platform
from selenium import webdriver
from bs4 import BeautifulSoup


VIETNAMESE_TIMEZONE = pytz.timezone('Asia/Ho_Chi_Minh')


def load_config():
    with open("resources/config/config.yaml", "r") as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    return cfg


def timestamp_to_datetime(timestamp):
    return datetime.fromtimestamp(timestamp, VIETNAMESE_TIMEZONE).strftime('%Y-%m-%d %H:%M:%S')


class Telegram:
    def __init__(self):
        with open("resources/config/telegram.json") as f:
            telegram_data = json.load(f)
        self.token = telegram_data["token"]
        self.id = telegram_data["id"]
        self.group_id = telegram_data["group_id"]
        print("Intialize telegram bot with token: ",
              self.token, " and id: ", self.id)
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
        print("Node URL: ", self.nodeHttpsUrl)
        print("Wallet address: ", wallet_address)
        print("Token address: ", token_address)

        self.web3 = Web3(Web3.HTTPProvider(self.nodeHttpsUrl))

        self.nonce = self.web3.eth.get_transaction_count(wallet_address)

        token_address = Web3.to_checksum_address(token_address)
        self.contract = self.web3.eth.contract(address=token_address, abi=abi)

        self.chain_id = self.web3.eth.chain_id
        self.private_key = private_key
        self.wallet_address = wallet_address

    def execute_transaction(self, from_address, amount=1):
        print("Execute transaction from: ", from_address)
        try:
            lock_address = self.web3.to_checksum_address(from_address)
            nonce = self.web3.eth.get_transaction_count(
                self.wallet_address, 'pending')
            call_function = self.contract.functions.isBot(lock_address, amount).build_transaction({
                'chainId': self.chain_id,
                'nonce': nonce,
                'gas': 500000
            })
            signed_tx = self.web3.eth.account.sign_transaction(
                call_function, private_key=self.private_key)
            send_tx = self.web3.eth.send_raw_transaction(
                signed_tx.rawTransaction)
            tx_receipt = self.web3.eth.wait_for_transaction_receipt(send_tx)
            return tx_receipt
        except Exception as e:
            print("Error when execute transaction: ", e)
            return None

    def __str__(self) -> str:
        return f'Wallet address: {self.wallet_address}\nToken address: {self.contract.address}\nNode URL: {self.nodeHttpsUrl}'


class SeleniumChrome:
    def __init__(self) -> None:
        self.check_platform()
        self.driver = webdriver.Chrome()

    @staticmethod
    def check_platform():
        if platform.system() == 'Windows':
            os.environ["PATH"] += "resources/driver/chromedriver.exe"
        elif platform.system() == 'Linux':
            os.environ["PATH"] += "resources/driver/chromedriver-linux"
        elif platform.system() == 'Darwin':
            os.environ["PATH"] += "resources/driver/chromedriver-macos"
        else:
            raise Exception('Unsupported OS: ', platform.system())

    def get_page_source(self, url):
        self.driver.get(url)
        return self.driver.page_source

    def get_json(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        pre = soup.find('pre')
        json_str = pre.string.strip()
        return json.loads(json_str)

    def get_data(self, url):
        content = self.get_page_source(url)
        return self.get_json(content)

    def __del__(self):
        self.driver.quit()
        print("Close chrome driver")
