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
        wine_dict['name'] = []
        wine_dict['production1'] = []
        wine_dict['production2'] = []
        wine_dict['production3'] = []
        wine_dict['production4'] = []
        wine_dict['type'] = []
        wine_dict['alc'] = []
        wine_dict['producer'] = []
        wine_dict['varieties'] = []
        wine_dict['bestfor'] = []
        wine_dict['sweetness'] = []
        wine_dict['body'] = []
        wine_dict['tastingnote'] = []

        for i in range(self.start, self.end):
            url = self.ulist.iloc[i]['URL']
            res = requests.get(url)
            soup = BeautifulSoup(res.content)

            idnum = re.search(r'\d{5}', url).group()
            wine_dict['id'].append(idnum)

            try:
                li0 = soup.find('li', attrs = {'class' : 'WineEndName'})
                wine_name = li0.get_text()
                subwine_name = re.sub(r'\s',' ', wine_name)
                wine_dict['name'].append(subwine_name)
            except:
                wine_dict['name'].append('None')

            try:
                li1 = soup.find('li', attrs = {'class' : 'WineProduction'})
                a = li1.find_all('a')
                for i in range(4):
                    if i <= len(a) -1 :
                        wine_dict['production{}'.format(i+1)].append(a[i].get_text())
                    else :
                        wine_dict['production{}'.format(i+1)].append('None')
            except:
                wine_dict['production1'].append('None')
                wine_dict['production2'].append('None')
                wine_dict['production3'].append('None')
                wine_dict['production4'].append('None')

            try:
                li1_1 = soup.find('li', attrs = {'class' : 'WineInfo'})
                words = li1_1.get_text().strip()
                wine_dict['type'].append(re.search(r'^\w+', words).group())
            except:
                wine_dict['type'].append('None')

            try:
                li = soup.find('li', attrs = {'class' : 'WineInfo'})
                aic = re.search(r'AIC[.\d]+', li.get_text().strip())
                if not aic :
                    wine_dict['alc'].append('None')
                else :
                    wine_dict['alc'].append(aic.group())
            except:
                wine_dict['alc'].append('None')

            try:
                li2 = soup.find('li', attrs = {'class' : 'Winery'})
                producer = li2.a.get_text()
                reproducer = re.sub(r'\s', ' ', producer)
                wine_dict['producer'].append(reproducer)
            except:
                wine_dict['producer'].append('None')

            try:
                li4 = soup.find('li', attrs = {'class' : 'BestFor'})
                bestfor = li4.get_text()
                wine_dict['bestfor'].append(bestfor.strip())
            except:
                wine_dict['bestfor'].append('None')


            try :
                li6 = soup.find('li', attrs = {'class' : 'Sweetness'})
                px = li6.find_all('img')[1]['style']
                wine_dict['sweetness'].append(re.search(r'\d+', px).group())
            except :
                wine_dict['sweetness'].append('None')

            try :
                li7 = soup.find('li', attrs = {'class' : 'Body'})
                px = li7.find_all('img')[1]['style']
                wine_dict['body'].append(re.search(r'\d+', px).group())
            except :
                wine_dict['body'].append('None')

        wine_df = pd.DataFrame(wine_dict)

        return wine_df

df = pd.read_csv('pd_url_list_short.csv')

i=17001
while i<17685:
    wine2 = GetText(df,i,i+685)
    result = wine2.wine_info()
    try:
        writer = pd.ExcelWriter('./wine{}_{}.xlsx'.format(i,i+685), engine=None)
        result.to_excel(writer, sheet_name='1', encoding ='utf-8')
        writer.save()
        i += 700
    except:
        i += 700
        continue
