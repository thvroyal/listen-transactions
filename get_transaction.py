from web3 import Web3
import time

transaction_hash = "0x86b639125d4e58e8b2f9353164366f51c4d847923815f2943a5669c955c460b9"

web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/4dd245ab4e1e4529acbcd3b5a81d02d4'))

for i in range(0, 10):
    t = time.time()
    result = web3.eth.get_transaction('0x1d11d87c66065e6cca9471e116b7e8af0c4f7acea4db9bb496c732c86f99458b')
    print("Time taken: ", time.time() - t)
    print(result)
