import pyupbit

access = "Ri8sxlJg25hn91uuMdxxdSu7nDV4TwaEJxfsU1Fp"          # 본인 값으로 변경
secret = "NnevoGtx8ySsTP3PXBxg2GU5XmMpT204mDF16AVd"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회    
print(pyupbit.get_tickers())