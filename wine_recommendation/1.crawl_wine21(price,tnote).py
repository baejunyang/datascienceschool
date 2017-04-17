from collections import OrderedDict
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

class GetText(object):
    def __init__(self, ulist, start, end):
        self.ulist = ulist
        self.start = start
        self.end = end

    def wine_info(self):
        wine_dict = OrderedDict()
        wine_dict['id'] = []
        wine_dict['varieties'] = []
        wine_dict['tastingnote0'] = []
        wine_dict['tastingnote1'] = []
        wine_dict['price'] = []

        for i in range(self.start, self.end):
            url = self.ulist.iloc[i]['URL']

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

            idnum = re.search(r'\d{5}', url).group()
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

        wine_df = pd.DataFrame(wine_dict)

        return wine_df

df = pd.read_csv('pd_url_list_short.csv')

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
