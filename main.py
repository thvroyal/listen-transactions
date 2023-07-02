import asyncio
from Crypto.Hash import keccak
from web3 import Web3
from python_socks import ProxyType
from web3_proxy_providers import AsyncSubscriptionWebsocketProvider
import yaml
import helpers
from datetime import datetime

# Load environment variables from .yaml file
with open("config.yaml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    
nodeHttpsUrl = cfg['INFURA_MAINNET_HTTPS_URL'] + cfg['INFURA_PROJECT_ID']
nodeWssUrl = cfg['INFURA_MAINNET_WSS_URL'] + cfg['INFURA_PROJECT_ID']
whiteList = cfg['WHITE_LIST']
web3 = Web3(Web3.HTTPProvider(nodeHttpsUrl))
telegram_bot = helpers.Telegram()

def do_something():
    pass

def get_transaction_info(transaction_hash):
    return web3.eth.get_transaction(transaction_hash)

async def callback(subs_id: str, json_result):
    # print("New event: ", json_result)
    transaction_hash = json_result['transactionHash']
    transaction_info = get_transaction_info(transaction_hash)
    from_address = transaction_info['from']
    to_address = transaction_info['to']
    print(f'From: {from_address}', f'To: {to_address}', sep='\n')
    if to_address.lower() == cfg["MAIN_WALLET"].lower():
        telegram_bot.send_message(f'New buy from {from_address} at {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}', is_group=True)
        if to_address.lower() in whiteList:
            do_something()

async def main(loop: asyncio.AbstractEventLoop):
    provider = AsyncSubscriptionWebsocketProvider(
        loop=loop,
        endpoint_uri=nodeWssUrl,
    )
    
    # subscribe to newHeads
    subscription_id = await provider.subscribe(
        [
            'logs',
            {
                "address": cfg["TOKEN_ADDRESS"].lower(),
                "topics": [],
            }
        ],
        callback
    )
    print(f'Subscribed with id {subscription_id}')
    
    # unsubscribe after 30 seconds
    await asyncio.sleep(30)
    await provider.unsubscribe(subscription_id)

if __name__ == '__main__':
    async_loop = asyncio.get_event_loop()
    while True:
        async_loop.run_until_complete(main(loop=async_loop))