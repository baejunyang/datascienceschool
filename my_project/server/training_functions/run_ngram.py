import pandas as pd
import functions as sf
import tfidf_functions as tf

X, y, weight = sf.cv_input()

#countvect no weight
recall = sf.RecallRate(X, y, tokenize=sf.tokenize_basic)
recall_multinomial = recall.multinomial(ngram=(1,2))
print '<basic tockenizer>'
print 'multinomial done'
recall_logistic = recall.logistic(ngram=(1,2))
print 'logistic done'
print '*' * 70

recall2 = sf.RecallRate(X, y, tokenize=sf.tokenize_filtered)
recall2_multinomial = recall2.multinomial(ngram=(1,2))
print '<filtered tockenizer>'
print 'multinomial done'
recall2_logistic = recall2.logistic(ngram=(1,2))
print 'logistic done'
print '*' * 70

recall3 = sf.RecallRate(X, y, tokenize=sf.tokenize_noun)
recall3_multinomial = recall3.multinomial(ngram=(1,2))
print '<filtered tockenizer>'
print 'multinomial done'
recall3_logistic = recall3.logistic(ngram=(1,2))
print 'logistic done'
print '*' * 70

dict1 = { 'multinomial_basic':recall_multinomial, 'logistic_basic':recall_logistic,
         'multinomial_filtered':recall2_multinomial, 'logistic_filtered':recall2_logistic,
         'multinomial_noun':recall3_multinomial, 'logistic_noun':recall3_logistic}
df = pd.DataFrame(dict1)
df.to_csv('ngram_no_weight.csv')

#countvect with weight
recall = sf.RecallRate(X, y, weight=weight, tokenize=sf.tokenize_basic)
recall_multinomial = recall.multinomial(ngram=(1,2))
recall_logistic = recall.logistic(ngram=(1,2))

recall2 = sf.RecallRate(X, y, tokenize=sf.tokenize_filtered)
recall2_multinomial = recall2.multinomial(ngram=(1,2))
recall2_logistic = recall2.logistic(ngram=(1,2))

recall3 = sf.RecallRate(X, y, tokenize=sf.tokenize_noun)
recall3_multinomial = recall3.multinomial(ngram=(1,2))
recall3_logistic = recall3.logistic(ngram=(1,2))

dict2 = {'multinomial_basic':recall_multinomial, 'logistic_basic':recall_logistic,
         'multinomial_filtered':recall2_multinomial, 'logistic_filtered':recall2_logistic,
         'multinomial_noun':recall3_multinomial, 'logistic_noun':recall3_logistic}
df = pd.DataFrame(dict2)
df.to_csv('ngram_with_weight.csv')

#tfidf no weight
recall = tf.RecallRate(X, y, tokenize=sf.tokenize_basic)
recall_multinomial = recall.multinomial(ngram=(1,2))
recall_logistic = recall.logistic(ngram=(1,2))

recall2 = tf.RecallRate(X, y, tokenize=sf.tokenize_filtered)
recall2_multinomial = recall2.multinomial(ngram=(1,2))
recall2_logistic = recall2.logistic(ngram=(1,2))

recall3 = tf.RecallRate(X, y, tokenize=sf.tokenize_noun)
recall3_multinomial = recall3.multinomial(ngram=(1,2))
recall3_logistic = recall3.logistic(ngram=(1,2))

dict1 = { 'multinomial_basic':recall_multinomial, 'logistic_basic':recall_logistic,
         'multinomial_filtered':recall2_multinomial, 'logistic_filtered':recall2_logistic,
         'multinomial_noun':recall3_multinomial, 'logistic_noun':recall3_logistic}
df = pd.DataFrame(dict1)
df.to_csv('tf_ngram_no_weight.csv')

#tfidf with weight
recall = tf.RecallRate(X, y, weight=weight, tokenize=sf.tokenize_basic)
recall_multinomial = recall.multinomial(ngram=(1,2))
recall_logistic = recall.logistic(ngram=(1,2))

recall2 = tf.RecallRate(X, y, tokenize=sf.tokenize_filtered)
recall2_multinomial = recall2.multinomial(ngram=(1,2))
recall2_logistic = recall2.logistic(ngram=(1,2))

recall3 = tf.RecallRate(X, y, tokenize=sf.tokenize_noun)
recall3_multinomial = recall3.multinomial(ngram=(1,2))
recall3_logistic = recall3.logistic(ngram=(1,2))

dict2 = {'multinomial_basic':recall_multinomial, 'logistic_basic':recall_logistic,
         'multinomial_filtered':recall2_multinomial, 'logistic_filtered':recall2_logistic,
         'multinomial_noun':recall3_multinomial, 'logistic_noun':recall3_logistic}
df = pd.DataFrame(dict2)
df.to_csv('tf_ngram_with_weight.csv')
