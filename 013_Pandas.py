# 13. Pandas를 이용한 데이터 분석 기초
# Pandas를 이용한 데이터 분석 기초
from pandas import Series
from pandas import DataFrame
from pandas_datareader.data as web
# pandas_datareader 패키지의 data 모듈은
# 인터넷상에서 제공하는 다양한 데이터를 DataFrame으로 만들어주는 기능 제공
import datatime
import matplotlib.pyplot as plt

##############################################
# 13.1.1 파이썬 리스트, 튜플, 딕셔너리
##############################################
mystock = ['kakao', 'naver']
print(mystock[0])
print(mystock[1])

# 리스트 좋은 점 : 반복문 사용이 쉬움, 다양한 메서드 제공
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
kakao_daily_ending_prices = {'2016-02-19' : 92600,
                            '2016-02-18' : 92400,
                            '2016-02-17' : 92100,
                            '2016-02-16' : 94300,
                            '2016-02-15' : 92300}
print(kakao_daily_ending_prices['2016-02-19'])


##############################################
# 13.1.2 Series 기초
##############################################

kakao = Series([92600, 92400, 92100, 94300, 92300])
print(kakao)    # Series 객체는 일차원 배열과는 달리 값 뿐만 아니라 각 값에 연결된 인덱스 값도 동시에 저장함.
print(kakao[0]) # 92600
# Series 객체는 파이썬 리스트와는 달리 인덱싱 값을 지정할 수 있음.
kakao2 = Series([92600, 92400, 92100, 94300, 92300]
                , index=['2016-02-19', '2016-02-18'
                        , '2016-02-17', '2016-02-16', '2016-02-15'])
print(kakao2)
print(kakao2[0])            # 92600
print(kakao2['2016-02-19']) # 92600, 정수값 대신 날짜문자열로 출력 가능

# Series 객체의 index와 value라는 이름의 속성을 통해 접근 가능.
for date in kakao2.index:
    print(date)
for ending_price in kakao2.values:
    print(ending_price)

# 주식보유현황
mine = Series([10, 20, 30], index=['naver', 'sk', 'kt'])
friend = Series([10, 30, 20], index=['kt', 'naver', 'sk'])

# pandas의 Series는 인덱싱이 서로 다른 경우에도 알아서
# 인덱싱이 같은 값끼리 덧셈 연산을 수행한다.
merge = mine + friend
print(merge)




##############################################
# 13.2 Pandas DataFrame
##############################################
# pandas의 Series가 1차원 형태의 자료구조라면,
# DataFrame은 여러 개의 칼럼(Column)으로 구성된 2차원 형태의 자료구조

# 1) DataFrame 생성
# DataFrame 객체 생성 가장 쉬운 방법 :
# 파이썬 딕셔너리 사용 → DataFrame클래스의 생성자 인자로 넘겨주기
raw_data = {'col0' : [1,2,3,4],
            'col1' : [10,20,30,40],
            'col2' : [100,200,300,400]}
type(raw_data)  # dict
data = DataFrame(raw_data)
print(data)
data['col0']
data['col1']
data['col2']
type(data['col0'])  # pandas.core.series.Series
# → 즉, DataFrame을 인덱스가 같은 여러 개의 Series 객체로 구성된 자료구조로 생각해도 좋음.

# DataFrame 객체의 내부구조
# 1. 'col0', 'col1', 'col2' 라는 세 개의 Series 객체로 구성되며, Series 객체의 인덱스는 동일함.
# 2. 하나의 파이썬 디셔너리 객체로 생각하기
# 2.1 DataFrame에는 3개의 Series 객체가 있고,
# 2.2 이는 'col0', 'col1', 'col2'라는 키에 각각 대응되는 값이고,
# 이것들을 하나의 파이썬 딕셔너리 객체로 생각하는 것
# 따라서 'col0', 'col1', 'col2'라는 키를 통해 값에 해당하는
# Series 객체에 접근할 수 있음.
daeshin = {'open':  [11650, 11100, 11200, 11100, 11000],
           'high':  [12100, 11800, 11200, 11100, 11150],
           'low' :  [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}
daeshin_day = DataFrame(daeshin)
print(daeshin_day)

# 칼럼 순서 지정
daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'])
# 인덱싱 값 지정
date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']
daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close']
                        , index=date)


# 2) DataFrame 칼럼, 로우 선택
close = daeshin_day['close']
print(daeshin_day['16.02.24'])  #'16.02.04'를 칼럼의 키 값으로 판단하여 에러처리
print(daeshin_day['close'])

# DataFrame 객체의 로우에 접근하기 : loc 메서드를 사용해 인덱스 값을 넘겨주기
day_data = daeshin_day.loc['16.02.24']
print(day_data)
print(type(day_data))   # <class 'pandas.core.series.Series'>

# 정리 : DataFrame 객체의 칼럼에 접근하려면 칼럼 이름을 지정하면 되고,
# 로우에 접근하려면 loc 메서드를 통해 인덱스 값을 지정하면 된다.
print(daeshin_day.columns)
print(daeshin_day.index)




##############################################
# 3) 주식 데이터 받기
##############################################
# 1) DataReader 사용하기
# DataReader를 이용해 야후 파이낸스로부터 GS 종목의 일봉 데이터를 받아와 보기
start = datetime.datetime(2016, 2, 19)
end = datetime.datetime(2016, 3, 4)

gs = web.DataReader("078930.KS", "yahoo", start, end)

# 2) 차트 그리기
start = datetime.datetime(2016, 2, 19)
end = datetime.datetime(2016, 3, 4)

gs = web.DataReader("078930.KS", "yahoo", start, end)
gs.info()

# 2010/1/1부터 데이터 조회한 날까지 데이터 얻어오기
gs = web.DataReader("078930.KS", "yahoo")
gs.info()

plt.plot(gs['Adj Close'])
plt.show()
# gs라는 DataFrame객체는 Data라는 인덱스를 사용하고 있으므로 이를 이용해 다시 그래프 그리기
gs.index

plt.plot(gs.index, gs['Adj Close'])
plt.show()





##############################################
# 4) 이동평균선 구하기
##############################################
# 2) Pandas를 이용한 주가이동평균 계산
gs = web.DataReader("078930.KS", "yahoo", "2014-01-01", "2016-03-06")
gs.tail()

# 수정 종가에 대해 5일 주가 이동평균 계산
ma5 = gs['Adj Close'].rolling(window=5).mean()
type(ma5)
ma5.tail(10)

# 3월 1일은 삼일절, 공휴일이므로 DataFrame객체에서 빼고 계산해야 함.
gs.tail()
new_gs = gs[gs['Volume'] != 0]
ma5 = new_gs['Adj Close'].rolling(window=5).mean()

# DataFrame 객체에 새로운 컬럼으로 추가하기
# insert 메서드 1번째 인자 : 컬럼추가위치, 2번째 인자 : 컬럼이름, 3번째 인자 : 추가할 데이터
ma5 = new_gs['Adj Close'].rolling(window=5).mean()
new_gs.insert(len(new_gs.columns), "MA5", ma5)
new_gs.tail(5)

# 20/60/120일 이동평균 값 컬럼 추가
ma20 = new_gs['Adj Close'].rolling(window=20).mean()
ma60 = new_gs['Adj Close'].rolling(window=60).mean()
ma120 = new_gs['Adj Close'].rolling(window=120).mean()

new_gs.insert(len(new_gs.columns), "MA20", ma20)
new_gs.insert(len(new_gs.columns), "MA60", ma60)
new_gs.insert(len(new_gs.columns), "MA120", ma120)

# Plot
plt.plot(new_gs.index, new_gs['Adj Close'], label='Adj Close')
plt.plot(new_gs.index, new_gs['MA5'], label='MA5')
plt.plot(new_gs.index, new_gs['MA20'], label='MA20')
plt.plot(new_gs.index, new_gs['MA60'], label='MA60')
plt.plot(new_gs.index, new_gs['MA120'], label='MA120')

plt.legend(loc="best")
plt.grid()
plt.show()