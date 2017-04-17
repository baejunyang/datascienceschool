import pandas as pd
import functions as sf
import tfidf_functions as tf

X, y, weight = sf.cv_input()

recall = sf.RecallRate(X, y, tokenize=sf.tokenize_basic)
recall_svc = recall.svc()
recall_multinomial = recall.multinomial()
recall_logistic = recall.logistic()

recall2 = sf.RecallRate(X, y, tokenize=sf.tokenize_filtered)
recall2_svc = recall2.svc()
recall2_multinomial = recall2.multinomial()
recall2_logistic = recall2.logistic()

recall3 = sf.RecallRate(X, y, tokenize=sf.tokenize_noun)
recall3_svc = recall3.svc()
recall3_multinomial = recall3.multinomial()
recall3_logistic = recall3.logistic()

dict1 = {'svc_basic':recall_svc, 'multinomial_basic':recall_multinomial, 'logistic_basic':recall_logistic,
        'svc_filtered':recall2_svc, 'multinomial_filtered':recall2_multinomial, 'logistic_filtered':recall2_logistic,
        'svc_noun':recall3_svc, 'multinomial_noun':recall3_multinomial, 'logistic_noun':recall3_logistic}
df = pd.DataFrame(dict1)
df.to_csv('no_weight.csv')

recall = RecallRate(X, y, weight=weight, tokenize=sf.tokenize_basic)
recall_svc = recall.svc()
recall_multinomial = recall.multinomial()
recall_logistic = recall.logistic()

recall2 = RecallRate(X, y, tokenize=sf.tokenize_filtered)
recall2_svc = recall2.svc()
recall2_multinomial = recall2.multinomial()
recall2_logistic = recall2.logistic()

recall3 = RecallRate(X, y, tokenize=sf.tokenize_noun)
recall3_svc = recall3.svc()
recall3_multinomial = recall3.multinomial()
recall3_logistic = recall3.logistic()

dict2 = {'svc_basic':recall_svc, 'multinomial_basic':recall_multinomial, 'logistic_basic':recall_logistic,
        'svc_filtered':recall2_svc, 'multinomial_filtered':recall2_multinomial, 'logistic_filtered':recall2_logistic,
        'svc_noun':recall3_svc, 'multinomial_noun':recall3_multinomial, 'logistic_noun':recall3_logistic}
df = pd.DataFrame(dict2)
df.to_csv('with_weight.csv')
