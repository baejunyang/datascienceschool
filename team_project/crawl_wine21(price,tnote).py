from collections import OrderedDict
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

class GetText(object):
    def __init__(self, ulist, start, end):                  #나중에 ulist 부분에는 앞에서 정의한 df를 넣어줍니다.
        self.ulist = ulist
        self.start = start
        self.end = end

    def wine_info(self):                        #wine_dict는 id, name, production 등등을 key로 갖는 사전.
        wine_dict = OrderedDict()               # 각각의 key는 리스트를 value로 갖습니다.
        wine_dict['id'] = []
        wine_dict['varieties'] = []
        wine_dict['tastingnote0'] = []
        wine_dict['tastingnote1'] = []
        wine_dict['price'] = []

        for i in range(self.start, self.end):                  # 크롤링할 범위 설정(wine_code가 아니라 인덱스 번호)
            url = self.ulist.iloc[i]['URL']          # self.ulist가 dataframe 형식이므로 iloc 이용해서 url을 가져옵니다.

            try:
                res = requests.get(url)
                soup = BeautifulSoup(res.content)
            except:
                wine_dict['id'].append('None')
                wine_dict['varieties'].append('None')
                wine_dict['tastingnote0'].append('None')
                wine_dict['tastingnote1'].append('None')
                wine_dict['price'].append('None')
                continue

            idnum = re.search(r'\d{5}', url).group()    #wine_code부터 크롤링 시작
            wine_dict['id'].append(idnum)

            try:
                li3 = soup.find('li', attrs = {'class' : 'Varieties'})
                varieties = ''
                for var in li3.find_all('a') :
                    varieties += var.get_text() + ','
                wine_dict['varieties'].append(varieties)
            except:
                wine_dict['varieties'].append('None')

            try:
                li = soup.find('li', {'class' : 'Price'})
                prices = li.find_all('div')[1].get_text()
                reprices = re.search(r'[-.,~\b\d]+', prices).group()
                wine_dict['price'].append(reprices)
            except:
                wine_dict['price'].append('None')

            try:
                div = soup.find('div', attrs = {'id' : 'TastingnoteCont'})
                note = div.find_all('li', attrs = {'class' : 'TastingnoteContent'})

                if len(note) == 2:
                    note0= note[0].get_text().strip()
                    subnote0= re.sub(r'\s', ' ', note0)
                    wine_dict['tastingnote0'].append(subnote0)

                    note1= note[1].get_text().strip()
                    subnote1 = re.sub(r'\s', ' ', note1)
                    wine_dict['tastingnote1'].append(subnote1)

                elif len(note) == 1:
                    wine_dict['tastingnote0'].append('None')

                    note1= note[1].get_text().strip()
                    subnote1 = re.sub(r'\s', ' ', note1)
                    wine_dict['tastingnote1'].append(subnote1)

            except:
                wine_dict['tastingnote0'].append('None')
                wine_dict['tastingnote1'].append('None')

        wine_df = pd.DataFrame(wine_dict)           # 사전 형식의 wine_dict를 dataframe 형식의 wine_df로 바꿔줍니다.

        return wine_df

df = pd.read_csv('pd_url_list_short.csv')       #df 변수로 csv 파일을 읽어옵니다.

starts = 1000
ends = 2000
clk = 1000
limit = 7000
while starts < limit:
    wine2 = GetText(df,starts,ends)              # wine2를 GetText의 객체로 설정. df는 csv 파일을 dataframe으로 변환한 것
    result = wine2.wine_info()
    try:
        writer = pd.ExcelWriter('./wines{}_{}.xlsx'.format(starts,ends), engine=None)
        result.to_excel(writer, sheet_name='1', encoding ='utf-8')      # 결과를 엑셀로 저장
        writer.save()
        starts += clk
        ends += clk
    except:
        starts += clk
        ends += clk
        continue
