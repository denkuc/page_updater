import time
from selenium.webdriver import Chrome

from telegram import telegram_client

# to now your Telegram id
last_chat_id = telegram_client.get_last_chat_id()
print(f'Your Telegram ID: {last_chat_id}')

while True:
    browser = Chrome()
    browser.get('https://france.mfa.gov.ua/timeline?&type=posts')

    # what you need to find
    browser.find_element()

    # select condition to exit the loop
    if "condition" == True:
        break
    else:
        browser.stop_client()
        time.sleep(20*60)

telegram_client.send_message('We found it!', last_chat_id)
