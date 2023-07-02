import asyncio
import json
from web3 import Web3
from websockets import connect
import yaml

# Load environment variables from .yaml file
with open("config.yaml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    
infura_http_url = cfg['INFURA_MAINNET_HTTPS_URL'] + cfg['INFURA_PROJECT_ID']
infura_ws_url = cfg['INFURA_MAINNET_WSS_URL'] + cfg['INFURA_PROJECT_ID']
web3 = Web3(Web3.HTTPProvider(infura_http_url))

# Used if you want to monitor ETH transactions to a specific address
account = cfg['TOKEN_ADDRESS'].lower()

async def get_event():
    async with connect(infura_ws_url) as ws:
        await ws.send('{"jsonrpc": "2.0", "id": 1, "method": "eth_subscribe", "params": ["newPendingTransactions"]}')
        # subscription_response = await ws.recv()

        while True:
            try:
                message = await asyncio.wait_for(ws.recv(), timeout=15)
                response = json.loads(message)
                txHash = response['params']['result']
                # print(txHash)
                # Uncomment lines below if you want to monitor transactions to
                # a specific address
                tx = web3.eth.get_transaction(txHash)
                if tx.to == account:
                    print("Pending transaction found with the following details:")
                    print({
                        "hash": txHash,
                        "from": tx["from"],
                        "value": web3.fromWei(tx["value"], 'ether')
                    })
                pass
            except:
                pass

if __name__ == "__main__":
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    loop = asyncio.get_event_loop()
    while True:
        loop.run_until_complete(get_event())