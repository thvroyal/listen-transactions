from bs4 import BeautifulSoup
import json
import telebot

def intersection(lst1, lst2): 
    return list(set(lst1) & set(lst2))

def get_all_transactions(html):
    soup = BeautifulSoup(html, "html.parser")
    all_transactions = soup.find_all("span", {"class": "hash-tag text-truncate myFnExpandBox_searchVal"})
    try:
        list_transactions = [transaction.text for transaction in all_transactions]
    except:
        list_transactions = []
    return list_transactions

class Telegram:
    def __init__(self):
        with open("telegram.json") as f:
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
        