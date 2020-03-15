# 13. Pandas를 이용한 데이터 분석 기초
# Pandas를 이용한 데이터 분석 기초
# 1) 파이썬 리스트, 튜플, 딕셔너리
mystock = ['kakao', 'naver']
print(mystock[0])
print(mystock[1])

# 리스트 좋은 점 : 반복문 사용이 쉬움
# 리스트 좋은 점: 다양한 메서드 제공
for stock in mystock:
    print(stock)


####################### 3장 참고 #######################
# 리스트 : [] 사용, 리스트 내의 원소를 변경할 수 있음. 메서드 활용 가능
# 튜플 : () 사용, 튜플 내의 원소를 변경할 수 없음. 리스트에 비해 속도 빠름
# 딕셔너리 : {} 사용, key와 value를 쌍으로 저장, 인덱싱 지원 x

kospi_top10 = ['삼성전자', 'SK하이닉스', '현대차', '한국전력'
                , '아모레퍼시픽', '제일모직', '삼성전자우', '삼성생명'
                , 'NAVER', '현대모비스']
print("시가총액 5위: ", kospi_top10[4])
# 데이터 삽입 : append
# 원하는 위치에 데이터 삽입 : insert
kospi_top10.append("SK텔레콤")
kospi_top10.insert(3, "셀트리온헬스케어") # 3번째 위치에 삽입(0,1,2,3)
len(kospi_top10)
kospi_top10[-1]

# 데이터 삭제 : del
del kospi_top10[-1]

# 튜플과 다른 점 : 리스트는 리스트 내의 원소를 변경할 수는 있지만, 튜플은 변경할 수 없다.
cur_price = {}
type(cur_price)

cur_price['daeshin'] = 30000
cur_price['Daum KAKAO'] = 80000
len(cur_price)  # 2
cur_price[0]    # 데이터를 순서대로 저장하는 것이 아니라 키와 값의 쌍이 서로 연결되도록만 저장
cur_price['daeshin']

del cur_price['daeshin']    # 딕셔너리 삭제
cur_price

cur_price = {'Daum KAKAO' : 80000, 'naver' : 800000, 'daeshin' : 30000}
cur_price.keys()
list(cur_price.keys()) # 리스트로 만들기
stock_list = list(cur_price.keys()) # 변수를 통해 list의 반환값을 바인딩
price_list = list(cur_price.values()) # 값 목록을 리스트로 만들어 바인딩

'Samsung' in cur_price.keys()
'naver' in cur_price.keys()
cur_price['Samsung']
####################### 3장 참고 끝 #######################



# 카카오 5일 간의 종가 데이터
kakao_daily_ending_prices = [92300, 94300, 92100, 92400, 92600]
for price in kakao_daily_ending_prices:
    print(price)
# 딕셔너리를 통해 날짜, 종가 데이터 각각 저장
kakao_daily_ending_price