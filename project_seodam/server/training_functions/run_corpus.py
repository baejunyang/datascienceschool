import pandas as pd
import functions as sf
import tfidf_functions as tf

#make corpus
corpus_basic=sf.make_corpus(tokenizer=sf.tokenize_basic)
corpus_filtered=sf.make_corpus(tokenizer=sf.tokenize_filtered)
corpus_noun=sf.make_corpus(tokenizer=sf.tokenize_noun)

#Using CountVectorizer
X, y, weight = sf.cv_input()

#without weight
basic = sf.ConfusionMatrix(X, y, tokenize=sf.tokenize_basic)
b_multi_report, b_multi_recall, b_multi_precision, b_multi_f1 = basic.multinomial(vocabulary=corpus_basic)
b_logistic_report, b_logistic_recall, b_logistic_precision, b_logistic_f1 = basic.logistic(vocabulary=corpus_basic)
print 'no weight basic tokenizer done (sf)'

filtered = sf.ConfusionMatrix(X, y, tokenize=sf.tokenize_filtered)
f_multi_report, f_multi_recall, f_multi_precision, f_multi_f1 = filtered.multinomial(vocabulary=corpus_filtered)
f_logistic_report, f_logistic_recall, f_logistic_precision, f_logistic_f1 = filtered.logistic(vocabulary=corpus_filtered)
print 'no weight filtered tokenizer (sf)'

noun = sf.ConfusionMatrix(X, y, tokenize=sf.tokenize_noun)
n_multi_report, n_multi_recall, n_multi_precision, n_multi_f1 = noun.multinomial(vocabulary=corpus_noun)
n_logistic_report, n_logistic_recall, n_logistic_precision, n_logistic_f1 = noun.logistic(vocabulary=corpus_noun)
print 'no weight noun tokenizer (sf)'

temp_dict = {'b_multi_recall':b_multi_recall, 'b_multi_precision':b_multi_precision, 'b_multi_f1':b_multi_f1,
            'f_multi_recall':f_multi_recall, 'f_multi_precision':f_multi_precision, 'f_multi_f1':f_multi_f1,
            'n_multi_recall':n_multi_recall, 'n_multi_precision':n_multi_precision, 'n_multi_f1':n_multi_f1,
            'b_logistic_recall':b_logistic_recall, 'b_logistic_precision':b_logistic_precision, 'b_logistic_f1':b_logistic_f1,
            'f_logistic_recall':f_logistic_recall, 'f_logistic_precision':f_logistic_precision, 'f_logistic_f1':f_logistic_f1,
            'n_logistic_recall':n_logistic_recall, 'n_logistic_precision':n_logistic_precision, 'n_logistic_f1':n_logistic_f1}
df = pd.DataFrame(temp_dict)
df.to_csv('count_noweight.csv')

#with weight
basic = sf.ConfusionMatrix(X, y, weight=weight, tokenize=sf.tokenize_basic)
b_multi_report, b_multi_recall, b_multi_precision, b_multi_f1 = basic.multinomial(vocabulary=corpus_basic)
b_logistic_report, b_logistic_recall, b_logistic_precision, b_logistic_f1 = basic.logistic(vocabulary=corpus_basic)
print 'with weigth basic tokenizer done (sf)'

filtered = sf.ConfusionMatrix(X, y, weight=weight, tokenize=sf.tokenize_filtered)
f_multi_report, f_multi_recall, f_multi_precision, f_multi_f1 = filtered.multinomial(vocabulary=corpus_filtered)
f_logistic_report, f_logistic_recall, f_logistic_precision, f_logistic_f1 = filtered.logistic(vocabulary=corpus_filtered)
print 'with weigth filtered tokenizer (sf)'

noun = sf.ConfusionMatrix(X, y, weight=weight, tokenize=sf.tokenize_noun)
n_multi_report, n_multi_recall, n_multi_precision, n_multi_f1 = noun.multinomial(vocabulary=corpus_noun)
n_logistic_report, n_logistic_recall, n_logistic_precision, n_logistic_f1 = noun.logistic(vocabulary=corpus_noun)
print 'with weigth noun tokenizer (sf)'

temp_dict = {'b_multi_recall':b_multi_recall, 'b_multi_precision':b_multi_precision, 'b_multi_f1':b_multi_f1,
            'f_multi_recall':f_multi_recall, 'f_multi_precision':f_multi_precision, 'f_multi_f1':f_multi_f1,
            'n_multi_recall':n_multi_recall, 'n_multi_precision':n_multi_precision, 'n_multi_f1':n_multi_f1,
            'b_logistic_recall':b_logistic_recall, 'b_logistic_precision':b_logistic_precision, 'b_logistic_f1':b_logistic_f1,
            'f_logistic_recall':f_logistic_recall, 'f_logistic_precision':f_logistic_precision, 'f_logistic_f1':f_logistic_f1,
            'n_logistic_recall':n_logistic_recall, 'n_logistic_precision':n_logistic_precision, 'n_logistic_f1':n_logistic_f1}
df = pd.DataFrame(temp_dict)
df.to_csv('count_weight.csv')


#Using TfidfVectorizer
X, y, weight = tf.cv_input()

#without weight
basic = tf.ConfusionMatrix(X, y, tokenize=tf.tokenize_basic)
b_multi_report, b_multi_recall, b_multi_precision, b_multi_f1 = basic.multinomial(vocabulary=corpus_basic)
b_logistic_report, b_logistic_recall, b_logistic_precision, b_logistic_f1 = basic.logistic(vocabulary=corpus_basic)
print 'no weight basic tokenizer done(tf)'

filtered = tf.ConfusionMatrix(X, y, tokenize=tf.tokenize_filtered)
f_multi_report, f_multi_recall, f_multi_precision, f_multi_f1 = filtered.multinomial(vocabulary=corpus_filtered)
f_logistic_report, f_logistic_recall, f_logistic_precision, f_logistic_f1 = filtered.logistic(vocabulary=corpus_filtered)
print 'no weight filtered tokenizer(tf)'

noun = tf.ConfusionMatrix(X, y, tokenize=tf.tokenize_noun)
n_multi_report, n_multi_recall, n_multi_precision, n_multi_f1 = noun.multinomial(vocabulary=corpus_noun)
n_logistic_report, n_logistic_recall, n_logistic_precision, n_logistic_f1 = noun.logistic(vocabulary=corpus_noun)
print 'no weight noun tokenizer(tf)'

temp_dict = {'b_multi_recall':b_multi_recall, 'b_multi_precision':b_multi_precision, 'b_multi_f1':b_multi_f1,
            'f_multi_recall':f_multi_recall, 'f_multi_precision':f_multi_precision, 'f_multi_f1':f_multi_f1,
            'n_multi_recall':n_multi_recall, 'n_multi_precision':n_multi_precision, 'n_multi_f1':n_multi_f1,
            'b_logistic_recall':b_logistic_recall, 'b_logistic_precision':b_logistic_precision, 'b_logistic_f1':b_logistic_f1,
            'f_logistic_recall':f_logistic_recall, 'f_logistic_precision':f_logistic_precision, 'f_logistic_f1':f_logistic_f1,
            'n_logistic_recall':n_logistic_recall, 'n_logistic_precision':n_logistic_precision, 'n_logistic_f1':n_logistic_f1}
df = pd.DataFrame(temp_dict)
df.to_csv('tf_noweight.csv')

#with weight
basic = tf.ConfusionMatrix(X, y, weight=weight, tokenize=tf.tokenize_basic)
b_multi_report, b_multi_recall, b_multi_precision, b_multi_f1 = basic.multinomial(vocabulary=corpus_basic)
b_logistic_report, b_logistic_recall, b_logistic_precision, b_logistic_f1 = basic.logistic(vocabulary=corpus_basic)
print 'with weigth basic tokenizer done(tf)'

filtered = tf.ConfusionMatrix(X, y, weight=weight, tokenize=tf.tokenize_filtered)
f_multi_report, f_multi_recall, f_multi_precision, f_multi_f1 = filtered.multinomial(vocabulary=corpus_filtered)
f_logistic_report, f_logistic_recall, f_logistic_precision, f_logistic_f1 = filtered.logistic(vocabulary=corpus_filtered)
print 'with weigth filtered tokenizer(tf)'

noun = tf.ConfusionMatrix(X, y, weight=weight, tokenize=tf.tokenize_noun)
n_multi_report, n_multi_recall, n_multi_precision, n_multi_f1 = noun.multinomial(vocabulary=corpus_noun)
n_logistic_report, n_logistic_recall, n_logistic_precision, n_logistic_f1 = noun.logistic(vocabulary=corpus_noun)
print 'with weigth noun tokenizer(tf)'

temp_dict = {'b_multi_recall':b_multi_recall, 'b_multi_precision':b_multi_precision, 'b_multi_f1':b_multi_f1,
            'f_multi_recall':f_multi_recall, 'f_multi_precision':f_multi_precision, 'f_multi_f1':f_multi_f1,
            'n_multi_recall':n_multi_recall, 'n_multi_precision':n_multi_precision, 'n_multi_f1':n_multi_f1,
            'b_logistic_recall':b_logistic_recall, 'b_logistic_precision':b_logistic_precision, 'b_logistic_f1':b_logistic_f1,
            'f_logistic_recall':f_logistic_recall, 'f_logistic_precision':f_logistic_precision, 'f_logistic_f1':f_logistic_f1,
            'n_logistic_recall':n_logistic_recall, 'n_logistic_precision':n_logistic_precision, 'n_logistic_f1':n_logistic_f1}
df = pd.DataFrame(temp_dict)
df.to_csv('tf_weight.csv')
