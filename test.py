import json
import requests
import pyupbit

access = "Ri8sxlJg25hn91uuMdxxdSu7nDV4TwaEJxfsU1Fp"
secret = "NnevoGtx8ySsTP3PXBxg2GU5X"
slack_token = "xoxb-2064130842913-2036913322215-iJgkwYNbHpjAKaK6bI0KMx0q"
channel = "#develop"

upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회

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
print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회    

count = 1
post_message(slack_token, channel, "autotrade start")
while count > 0:
    post_message(slack_token, channel, "message test" + str(count) + str(upbit.get_balance("KRW")))
    count = count-1
    
