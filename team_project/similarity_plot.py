df_distance = pd.read_csv('./team3/distance_test.csv')

leng = d2['distance_0']   #유클리드 유사도
cos = d2['cosine_0']      #코사인 유사도

x = cos * leng
y = np.sqrt(leng**2 - x**2)

#원점과의 거리가 유클리드 거리를 나타내고, x축과의 거리가 코싸인 유사도를 나타낸다.
plt.scatter(x,y)
plt.xlim(2,3)
plt.ylim(0.5,2.5)
plt.grid(True)
plt.show()
