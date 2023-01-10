import requests 
from bs4 import BeautifulSoup as bs
import math, re
import pandas as pd 
from datetime import date, timedelta
from check_weekend import check_weekend
        
day = check_weekend()
day = day[0:4] + day[5:7] + day[-2:]  

bond_url = 'http://apis.data.go.kr/1160100/service/GetBondSecuritiesInfoService'
encoding_key = ""
decoding_key = ""

res_bond_url = bond_url + '/getBondPriceInfo?serviceKey=' + decoding_key + "&pageNo=1&numOfRows=1&resultType=xml&basDt=" + day 

res = requests.get(res_bond_url)    
res_text = res.text
xml_parser = bs(res_text, 'xml')

# 전체 종목 가져오기 위해서 전체 페이지 수 구하기 
# total_N = xml_parser.select_one('totalCount').get_text()

# '종목명'/'시가 가격' 저장할 리스트 선언 
itmsNm_list = []
mkpPrc_list = []

# page_N = math.floor(int(total_N)/10) + 1  # 한 페이지에 10 개씩 가져올 거라서 /10 해줌 

for n in range(1, 5): 
    res_bond_url = bond_url + '/getBondPriceInfo?serviceKey=' + decoding_key + "&pageNo=" + str(n)+ "&numOfRows=10&resultType=xml" 
    
    res = requests.get(res_bond_url)    
    res_text = res.text
    xml_parser = bs(res_text, 'xml')
    
    # itmsNm 값을 itmsNS list 에 저장 
    for i in xml_parser.select('itmsNm'):
        itmsNm_list.append((re.sub(" ", "", i.get_text())))
    # mkpPrc 값을 mkpPrc list 에 저장
    for i in xml_parser.select('mkpPrc'):
        mkpPrc_list.append((re.sub(" ", "", i.get_text())))

        
# 데이터 프레임으로 정리 

df_bond = pd.DataFrame() 
df_bond['itmsNM'] = itmsNm_list
df_bond['mkpPrc'] = mkpPrc_list

bond_data = df_bond.columns.values.tolist()

# print(df_bond)

def bondData():
    return df_bond 