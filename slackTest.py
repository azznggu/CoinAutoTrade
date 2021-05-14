import json
import requests
import time
import pyupbit

access = "Ri8sxlJg25hn91uuMdxxdSu7nDV4TwaEJxfsU1Fp"          # 본인 값으로 변경
secret = "NnevoGtx8ySsTP3PXBxg2GU5XmMpT204mDF16AVd"          # 본인 값으로 변경
slack_token = "xoxb-2064130842913-2036913322215-iJgkwYNbHpjAKaK6bI0KMx0q"
channel = "#develop"


def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

def get_balance(coin):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == coin:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
                


upbit = pyupbit.Upbit(access, secret)
count = 3

post_message(slack_token, channel, "BTC balance: "+ str(upbit.get_balance("KRW-BTC")))

# post_message(slack_token, channel, "autotrade start")
while count > 0:
    post_message(slack_token, channel, "BTC current price: "+ str(pyupbit.get_current_price("KRW-BTC")) + str(count))
    count = count-1
    time.sleep(10)
    
