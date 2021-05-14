
import pyupbit
import numpy as np

# OHLCV(open, high, low, close, volume)로 당일 시가, 고가, 저가, 종가, 거래량 데이터 취득
df = pyupbit.get_ohlcv("KRW-XRP", count=3)

# # 전략부분
# 변동성 돌파 기준 범위 계산 (고가 - 저가) * k값
df['range'] = (df['high'] - df['low']) * 0.5
# target(매수가), range 컬럼을 한칸씩 밑으로 내림 (shift(1))
df['target'] = df['open'] + df['range'].shift(1)


# # 기본설정부분
# 수수료 설정
fee = 0

# ror(수익률), np.where(조건문, 참일때 값, 거짓일때 값)
df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target'] - fee, 1)

# 누적 곱 계산(cumprod) => 누적 수익률
df['hpr'] = df['ror'].cumprod()

# Drw Down 계산 (누적 최대값과 현재 hpr 차이 / 누적 최대값 * 100)
# 낙폭, 특정 기간 동안 발생한 시세 고점에서 저점까지의 하락
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

# MDD계산
# 맥시멈 드로우다운(Maximum Drawdown), 최대 낙폭
# 시세가 새 고점에 도달하기 전에 그 이전 고점에서 저점까지의 최대 손실을 의미
print("MDD(%): ", df['dd'].max())

# 엑셀 출력
df.to_excel("xrp-3day.xlsx")