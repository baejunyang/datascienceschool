import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt

df = pd.read_csv('./team3/wine_data_climate.csv')  #숫자로 인코딩 된 dataset.
data_pool = np.array(df.ix[:,1:])                  #0번째 컬럼은 id

x_new = data_pool[0]
distance = np.linalg.norm(data_pool - x_new, axis=1)
df['distance_0']=distance
cosine = cosine_similarity(data_pool, x_new)
df['cosine_0']=cosine

df.to_csv('distance_test.csv')
