import FinanceDataReader as fdr
import pandas_ta as ta
import pandas as pd
import matplotlib. pyplot as plt

# 원하는 기업 코드
company_code = '005930'  #삼성전자
# 해당기업의 시계열 주가
company_price_df = fdr.DataReader(company_code, '1970')

# algorithm
# 20ema 200sma goldencross/deadcross

company_price_df['60ema'] = ta.ema(company_price_df['Close'], length=60)  # 지수이평
company_price_df['200sma'] = ta.sma(company_price_df['Close'], length=200)   # 단순이평
company_price_df = company_price_df.dropna()  # N/A인 부분은 날리기

# 매매시점을 찾아보자
buy_dt = []
sell_dt = []
for dt1, dt2, dt3, dt4, dt5 in zip(company_price_df.index[0:], company_price_df.index[1:], company_price_df.index[2:], company_price_df.index[3:], company_price_df.index[4:]):
    if (company_price_df.loc[dt1]['60ema'] < company_price_df.loc[dt1]['200sma'] and company_price_df.loc[dt2]['60ema'] < company_price_df.loc[dt2]['200sma'])\
        and company_price_df.loc[dt3]['60ema'] > company_price_df.loc[dt3]['200sma'] and company_price_df.loc[dt4]['60ema'] > company_price_df.loc[dt4]['200sma']:
        buy_dt.append(dt5)
    if (company_price_df.loc[dt1]['60ema'] > company_price_df.loc[dt1]['200sma'] and company_price_df.loc[dt2]['60ema'] > company_price_df.loc[dt2]['200sma'])\
        and company_price_df.loc[dt3]['60ema'] < company_price_df.loc[dt3]['200sma'] and company_price_df.loc[dt4]['60ema'] < company_price_df.loc[dt4]['200sma']:
        sell_dt.append(dt5)