import requests 
import time
from datetime import datetime
from sys import getsizeof
import helpers
from collections import deque


with open("token.txt") as f:
    token = f.read()

url = "https://etherscan.io/address/" + token
header = {"User-Agent": "Mozilla/5.0"}

if __name__ == "__main__":
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    telegram_bot = helpers.Telegram()    
    count = 0
    old_list_transactions = deque(maxlen=100)
    is_first = True
    while True:
        try:
            count += 1
            t = time.time()
            response = requests.get(url, headers=header).text
            size_of_response = getsizeof(response)
            total_time = time.time() - t
            # print("Count: " + str(count) + " Time requests: " + str(total_time) + " Size: " + str(size_of_response))
            if size_of_response < 100000:
                print("Failed")
                with open("fail.html", "w") as f:
                    f.write(response)
                break
            list_transactions = helpers.get_all_transactions(response)
            if is_first:
                old_list_transactions.extend(list_transactions)
                is_first = False
            intersection = helpers.intersection(old_list_transactions, list_transactions)
            new_transactions = [transaction for transaction in list_transactions if transaction not in intersection]
            if len(new_transactions) > 0:
                print("Date time: " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                print("New transactions: ", new_transactions)
                message = "Date time: " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + "\n" + "New transactions: "
                for transaction in new_transactions:
                    message += "\n" + transaction
                telegram_bot.send_message(message, is_group=True)
                old_list_transactions.extend(new_transactions)
                print("Total new transactions: " + str(len(new_transactions)))
                print("*" * 10)
            if total_time < 1:
                time.sleep(1 - total_time)
        except:
            print("Failed request")