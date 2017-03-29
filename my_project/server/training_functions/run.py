import pandas as pd
import functions as sf
from functions import RecallRate, FalseSamples

X, y, weight = sf.cv_input()

recall = RecallRate(X, y, tokenize=sf.tokenize_basic)
recall_svc = recall.svc()
recall_multinomial = recall.multinomial()
recall_logistic = recall.logistic()

recall2 = RecallRate(X, y, tokenize=sf.tokenize_filtered)
recall2_svc = recall.svc()
recall2_multinomial = recall.multinomial()
recall2_logistic = recall.logistic()

recall3 = RecallRate(X, y, tokenize=sf.tokenize_noun)
recall3_svc = recall.svc()
recall3_multinomial = recall.multinomial()
recall3_logistic = recall.logistic()

dict1 = {'svc_basic':recall_svc, 'multinomial_basic':recall_multinomial, 'logistic_basic':recall_logistic,
        'svc_filtered':recall2_svc, 'multinomial_filtered':recall2_multinomial, 'logistic_filtered':recall2_logistic,
        'svc_noun':recall3_svc, 'multinomial_noun':recall3_multinomial, 'logistic_noun':recall3_logistic}
df = pd.DataFrame(dict1)
df.to_csv('test.csv')

