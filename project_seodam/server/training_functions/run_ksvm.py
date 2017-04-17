import pandas as pd
import functions as sf
import tfidf_functions as tf

#Using CountVectorizer
X, y, weight = sf.cv_input()

#without weight
basic = sf.ConfusionMatrix(X, y, tokenize=sf.tokenize_basic)
b_ksvm1_report, b_ksvm1_recall, b_ksvm1_precision, b_ksvm1_f1 = basic.svc()
b_ksvm10_report, b_ksvm10_recall, b_ksvm10_precision, b_ksvm10_f1 = basic.svc(gamma=10)
print 'no weight basic tokenizer done (sf)'

filtered = sf.ConfusionMatrix(X, y, tokenize=sf.tokenize_filtered)
f_ksvm1_report, f_ksvm1_recall, f_ksvm1_precision, f_ksvm1_f1 = filtered.svc()
f_ksvm10_report, f_ksvm10_recall, f_ksvm10_precision, f_ksvm10_f1 = filtered.svc(gamma=10)
print 'no weight filtered tokenizer (sf)'

temp_dict = {'b_ksvm1_recall':b_ksvm1_recall, 'b_ksvm1_precision':b_ksvm1_precision, 'b_ksvm1_f1':b_ksvm1_f1,
            'f_ksvm1_recall':f_ksvm1_recall, 'f_ksvm1_precision':f_ksvm1_precision, 'f_ksvm1_f1':f_ksvm1_f1,
            'b_ksvm10_recall':b_ksvm10_recall, 'b_ksvm10_precision':b_ksvm10_precision, 'b_ksvm10_f1':b_ksvm10_f1,
            'f_ksvm10_recall':f_ksvm10_recall, 'f_ksvm10_precision':f_ksvm10_precision, 'f_ksvm10_f1':f_ksvm10_f1}
df = pd.DataFrame(temp_dict)
df.to_csv('ksvm_count_noweight.csv')

#with weight
basic = sf.ConfusionMatrix(X, y, weight=weight, tokenize=sf.tokenize_basic)
b_ksvm1_report, b_ksvm1_recall, b_ksvm1_precision, b_ksvm1_f1 = basic.svc()
b_ksvm10_report, b_ksvm10_recall, b_ksvm10_precision, b_ksvm10_f1 = basic.svc(gamma=10)
print 'with weigth basic tokenizer done (sf)'

filtered = sf.ConfusionMatrix(X, y, weight=weight, tokenize=sf.tokenize_filtered)
f_ksvm1_report, f_ksvm1_recall, f_ksvm1_precision, f_ksvm1_f1 = filtered.svc()
f_ksvm10_report, f_ksvm10_recall, f_ksvm10_precision, f_ksvm10_f1 = filtered.svc(gamma=10)
print 'with weigth filtered tokenizer (sf)'

temp_dict = {'b_ksvm1_recall':b_ksvm1_recall, 'b_ksvm1_precision':b_ksvm1_precision, 'b_ksvm1_f1':b_ksvm1_f1,
            'f_ksvm1_recall':f_ksvm1_recall, 'f_ksvm1_precision':f_ksvm1_precision, 'f_ksvm1_f1':f_ksvm1_f1,
            'b_ksvm10_recall':b_ksvm10_recall, 'b_ksvm10_precision':b_ksvm10_precision, 'b_ksvm10_f1':b_ksvm10_f1,
            'f_ksvm10_recall':f_ksvm10_recall, 'f_ksvm10_precision':f_ksvm10_precision, 'f_ksvm10_f1':f_ksvm10_f1}
df = pd.DataFrame(temp_dict)
df.to_csv('ksvm_count_weight.csv')


#Using TfidfVectorizer
X, y, weight = tf.cv_input()

#without weight
basic = tf.ConfusionMatrix(X, y, tokenize=tf.tokenize_basic)
b_ksvm1_report, b_ksvm1_recall, b_ksvm1_precision, b_ksvm1_f1 = basic.svc()
b_ksvm10_report, b_ksvm10_recall, b_ksvm10_precision, b_ksvm10_f1 = basic.svc(gamma=10)
print 'no weight basic tokenizer done(tf)'

filtered = tf.ConfusionMatrix(X, y, tokenize=tf.tokenize_filtered)
f_ksvm1_report, f_ksvm1_recall, f_ksvm1_precision, f_ksvm1_f1 = filtered.svc()
f_ksvm10_report, f_ksvm10_recall, f_ksvm10_precision, f_ksvm10_f1 = filtered.svc(gamma=10)
print 'no weight filtered tokenizer(tf)'

temp_dict = {'b_ksvm1_recall':b_ksvm1_recall, 'b_ksvm1_precision':b_ksvm1_precision, 'b_ksvm1_f1':b_ksvm1_f1,
            'f_ksvm1_recall':f_ksvm1_recall, 'f_ksvm1_precision':f_ksvm1_precision, 'f_ksvm1_f1':f_ksvm1_f1,
            'b_ksvm10_recall':b_ksvm10_recall, 'b_ksvm10_precision':b_ksvm10_precision, 'b_ksvm10_f1':b_ksvm10_f1,
            'f_ksvm10_recall':f_ksvm10_recall, 'f_ksvm10_precision':f_ksvm10_precision, 'f_ksvm10_f1':f_ksvm10_f1}
df = pd.DataFrame(temp_dict)
df.to_csv('ksvm_tf_noweight.csv')

#with weight
basic = tf.ConfusionMatrix(X, y, weight=weight, tokenize=tf.tokenize_basic)
b_ksvm1_report, b_ksvm1_recall, b_ksvm1_precision, b_ksvm1_f1 = basic.svc()1
b_ksvm10_report, b_ksvm10_recall, b_ksvm10_precision, b_ksvm10_f1 = basic.svc(gamma=10)
print 'with weigth basic tokenizer done(tf)'

filtered = tf.ConfusionMatrix(X, y, weight=weight, tokenize=tf.tokenize_filtered)
f_ksvm1_report, f_ksvm1_recall, f_ksvm1_precision, f_ksvm1_f1 = filtered.svc()
f_ksvm10_report, f_ksvm10_recall, f_ksvm10_precision, f_ksvm10_f1 = filtered.svc(gamma=10)
print 'with weigth filtered tokenizer(tf)'

temp_dict = {'b_ksvm1_recall':b_ksvm1_recall, 'b_ksvm1_precision':b_ksvm1_precision, 'b_ksvm1_f1':b_ksvm1_f1,
            'f_ksvm1_recall':f_ksvm1_recall, 'f_ksvm1_precision':f_ksvm1_precision, 'f_ksvm1_f1':f_ksvm1_f1,
            'b_ksvm10_recall':b_ksvm10_recall, 'b_ksvm10_precision':b_ksvm10_precision, 'b_ksvm10_f1':b_ksvm10_f1,
            'f_ksvm10_recall':f_ksvm10_recall, 'f_ksvm10_precision':f_ksvm10_precision, 'f_ksvm10_f1':f_ksvm10_f1}
df = pd.DataFrame(temp_dict)
df.to_csv('ksvm_tf_weight.csv')
