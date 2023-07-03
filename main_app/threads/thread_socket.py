import asyncio
import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
import yaml
from web3_proxy_providers import AsyncSubscriptionWebsocketProvider
from collections import deque
from datetime import datetime


class ThreadSocket(QtCore.QThread):
    def __init__(self, parent=None, token=..., transaction_queue=...):
        super().__init__(parent)
        self.__is_running = False
        self.transaction_queue = transaction_queue
        
        cfg = self.load_config()
        self.nodeHttpsUrl = cfg['INFURA_MAINNET_HTTPS_URL'] + cfg['INFURA_PROJECT_ID']
        self.nodeWssUrl = cfg['INFURA_MAINNET_WSS_URL'] + cfg['INFURA_PROJECT_ID']
        self.whiteList = cfg['WHITE_LIST']
        self.token = token.lower()
        
        self.old_transaction_hashes = deque(maxlen=100)
        
    @staticmethod
    def load_config():
        with open("resources/config/config.yaml", "r") as ymlfile:
            cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
        return cfg

    async def callback(self, subs_id: str, json_result):
        transaction_hash = json_result["transactionHash"]
        if transaction_hash not in self.old_transaction_hashes:
            self.old_transaction_hashes.append(transaction_hash)
            datetime_now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            self.transaction_queue.put([datetime_now, transaction_hash])
            print("New transaction: ", datetime_now, transaction_hash)
        
    async def main(self, loop: asyncio.AbstractEventLoop):
        provider = AsyncSubscriptionWebsocketProvider(
            loop=loop,
            endpoint_uri=self.nodeWssUrl
        )

        # subscribe to newHeads
        subscription_id = await provider.subscribe(
            [
                'logs',
                {
                    "address": self.token,
                    "topics": [],
                }
            ],
            self.callback
        )
        print(f'Subscribed with id {subscription_id}, address: {self.token}')

        # unsubscribe after 30 seconds
        await asyncio.sleep(30)
        await provider.unsubscribe(subscription_id)
        
    def run(self):
        self.__is_running = True
        print("Thread started")
        while self.__is_running:
            loop = asyncio.new_event_loop()
            loop.run_until_complete(self.main(loop=loop))
            loop.stop()
    
    def stop(self):
        self.__is_running = False