import numpy as np
import pandas as pd
import re
from collections import OrderedDict

tn = pd.read_csv('tnote0302.csv')           #tnote0302 : 와인별 tasting note 텍스트
tn.columns = ['num', 'id', 'note']
sm = pd.read_csv('./team3/smell_short.csv') #smell_short : 14개 향기 카테고리 구분과 카테고리별 해당하는 단어

encd_df = pd.DataFrame(sm.columns)
for k in range(17686):
    encd = np.zeros(14)                    #각 와인별
    for j in range(14):                    #각 카테고리별
        for i in sm.ix[:,j]:               #카테고리의 향기별
            if str(i) in tn.ix[k,1]:
                encd[j] += 1
    encd_df[tn.ix[k,0]] = encd
encd_df.to_csv('encoding0223.csv')
