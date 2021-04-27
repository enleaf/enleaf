import pyupbit

access = "IqbeH7s3R6ULojsMDEx5UeREvTWNmvWR75y9I4RU"          # 본인 값으로 변경
secret = "ofzFG03attOxsPIhmbWVsSnrXQ8bsQWjOV4nxJWP"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print("비트코인 조회 : ",upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print("이더리움 조회 : ",upbit.get_balance("KRW-ETH"))     # KRW-XRP 조회
print("보유현금 조회 : ",upbit.get_balance("KRW"))         # 보유 현금 조회