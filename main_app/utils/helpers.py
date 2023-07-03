import json
import telebot
import yaml


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
        