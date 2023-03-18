import json
import requests
from urllib import parse

TOKEN = "BOT_TOKEN"
URL = f"https://api.telegram.org/bot{TOKEN}/"


class Telegram:
    @staticmethod
    def get_url(url):
        response = requests.get(url)
        content = response.content.decode("utf8")
        return content

    def get_json_from_url(self, url):
        content = self.get_url(url)
        js = json.loads(content)
        return js

    def get_updates(self):
        url = URL + "getUpdates"
        js = self.get_json_from_url(url)
        return js

    def get_last_chat_id(self):
        chat_id = self.get_updates()["result"][-1]["message"]["chat"]["id"]
        print(chat_id)

    def send_message(self, text, chat_id):
        text = parse.quote_plus(text)
        url = f"{URL}sendMessage?text={text}&chat_id={chat_id}&parse_mode=Markdown"
        self.get_url(url)


telegram_client = Telegram()
