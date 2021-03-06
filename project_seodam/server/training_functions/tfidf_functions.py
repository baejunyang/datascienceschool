import pandas as pd
import numpy as np
from konlpy.tag import Twitter
from sklearn.model_selection import train_test_split
from sklearn.cross_validation import StratifiedKFold, ShuffleSplit, cross_val_score
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix

def cv_input(frozen_dir='../../private/files/seodam_together_notags0326.csv', unfrozen_dir='../../private/files/unfrozen_mixed0402.csv', row_limit=3211):
    df_frozen = pd.read_csv(frozen_dir).drop(['Unnamed: 0'], axis=1)
    df_unfrozen = pd.read_csv(unfrozen_dir).drop(['Unnamed: 0'], axis=1)[:row_limit]

    unfrozen = np.array(df_unfrozen['text2'])
    frozen = np.array(df_frozen['text'])

    weight0 = np.append(np.array(np.ones(row_limit, dtype=int)), np.array(df_frozen['freeze']))
    seodam_x = np.append(unfrozen, frozen)
    seodam_y = np.append(np.zeros(row_limit, dtype=int), np.ones(row_limit, dtype=int))
    return (seodam_x, seodam_y, weight0)

def make_stopwords(stwd_dir='stopwords.txt'):
    stop_words = []
    with open(stwd_dir, 'r') as reader :
        stop_words0 = reader.readlines()
        stop_words1 = stop_words0[0].split(',')
    for words in stop_words1:
        stop_words.append(words.decode('utf-8'))
    return stop_words

def tokenize_basic(doc):
    pos_tagger = Twitter()
    return ['/'.join(t) for t in pos_tagger.pos(doc, norm=True, stem=True)]

def tokenize_noun(doc):
    pos_tagger = Twitter()
    return pos_tagger.nouns(doc)

def tokenize_filtered(doc):
    tagger = Twitter()
    token_list = []
    for t in tagger.pos(doc, norm=True, stem=True):
        if t[1] != 'Josa' and t[1] != 'Punctuation' and t[1] != 'Determiner' and t[1] != 'URL' :
            token_list.append('/'.join(t))
    return token_list

def make_corpus(tokenizer=tokenize_basic, corpus='../corpus.txt'):
    with open('corpus.txt', 'r') as corp:
        corpus0 = corp.read().decode('utf-8')
    corpus = tokenizer(corpus0)
    return corpus

class RecallRate(object):
    def __init__(self, X, y, tokenize=tokenize_filtered, weight=None, stop_words=None, len_row=6422, random_state=0):
        self.X = X
        self.y = y
        self.tokenize = tokenize
        self.weight = weight
        self.stop_words = stop_words
        self.len_row = len_row
        self.random_state = random_state

    def svc(self, knl='linear'):
        model = Pipeline([
                ('vect', TfidfVectorizer(tokenizer=self.tokenize, stop_words=self.stop_words)),
                ('clf', SVC(kernel=knl))])
        cv = ShuffleSplit(self.len_row, random_state=self.random_state)
        recall_rate = cross_val_score(model, self.X, self.y, scoring='recall', cv=cv, fit_params={'clf__sample_weight' : self.weight})
        return recall_rate

    def multinomial(self, ngram=(1,1)):
        model = Pipeline([
                ('vect', TfidfVectorizer(tokenizer=self.tokenize, stop_words=self.stop_words, ngram_range=ngram)),
                ('clf', MultinomialNB())])
        cv = ShuffleSplit(self.len_row, random_state=self.random_state)
        recall_rate = cross_val_score(model, self.X, self.y, scoring='recall', cv=cv, fit_params={'clf__sample_weight' : self.weight})
        return recall_rate

    def logistic(self, ngram=(1,1)):
        model = Pipeline([
                ('vect', TfidfVectorizer(tokenizer=self.tokenize, stop_words=self.stop_words, ngram_range=ngram)),
                ('clf', LogisticRegression())])
        cv = ShuffleSplit(self.len_row, random_state=self.random_state)
        recall_rate = cross_val_score(model, self.X, self.y, scoring='recall', cv=cv, fit_params={'clf__sample_weight' : self.weight})
        return recall_rate

class FalseSamples(object):
    def __init__(self, X, y, w, tokenize=tokenize_filtered, weight=False, stop_words=None, random_state=0):
        self.X = X
        self.y = y
        self.w = w
        self.tokenize = tokenize
        self.weight = weight
        self.stop_words = stop_words
        self.random_state = random_state

    def simple_split(self):
        X_train, X_test, y_train, y_test, w_train, w_test = train_test_split(self.X, self.y, self.w, test_size=0.1, random_state=self.random_state)
        return X_train, X_test, y_train, y_test, w_train

    def svc(self, knl='linear'):
        X_train, X_test, y_train, y_test, w_train = simple_split()
        model = Pipeline([
                ('vect', TfidfVectorizer(tokenizer=self.tokenize, stop_words=self.stop_words)),
                ('clf', SVC(kernel=knl))])

        if self.weight == False :
            w_train = None
        model.fit(X_train, y_train, **{'clf__sample_weight' : w_train})
        result = model.predict(X_test)

        mask_fn = np.logical_and(y_test==0, result==1)
        mask_fp = np.logical_and(y_test==1, result==0)

        false_negative = [text.decode('utf-8') for text in X_text[mask_fn]]
        false_positive = [text.decode('utf-8') for text in X_test[mask_fp]]

        report = confusion_matrix(y_test, result)
        recall_rate = float(report[1,1]) / (report[1,0] + report[1,1])
        return recall_rate, false_negative, false_positive

    def multinomial(self, ngram=(1,1)):
        X_train, X_test, y_train, y_test, w_train = simple_split()
        model = Pipeline([
                ('vect', TfidfVectorizer(tokenizer=self.tokenize, stop_words=self.stop_words, ngram_range=ngram)),
                ('clf', MultinomialNB())])

        if self.weight == False :
            w_train = None
        model.fit(X_train, y_train, **{'clf__sample_weight' : w_train})
        result = model.predict(X_test)

        mask_fn = np.logical_and(y_test==0, result==1)
        mask_fp = np.logical_and(y_test==1, result==0)

        false_negative = [text.decode('utf-8') for text in X_text[mask_fn]]
        false_positive = [text.decode('utf-8') for text in X_test[mask_fp]]

        report = confusion_matrix(y_test, result)
        recall_rate = float(report[1,1]) / (report[1,0] + report[1,1])
        return recall_rate, false_negative, false_positive

    def logistic(self, ngram=(1,1)):
        X_train, X_test, y_train, y_test, w_train = simple_split()
        model = Pipeline([
                ('vect', TfidfVectorizer(tokenizer=self.tokenize, stop_words=self.stop_words, ngram_range=ngram)),
                ('clf', LogisticRegression())])

        if self.weight == False :
            w_train = None
        model.fit(X_train, y_train, **{'clf__sample_weight' : w_train})
        result = model.predict(X_test)

        mask_fn = np.logical_and(y_test==0, result==1)
        mask_fp = np.logical_and(y_test==1, result==0)

        false_negative = [text.decode('utf-8') for text in X_text[mask_fn]]
        false_positive = [text.decode('utf-8') for text in X_test[mask_fp]]

        report = confusion_matrix(y_test, result)
        recall_rate = float(report[1,1]) / (report[1,0] + report[1,1])
        return recall_rate, false_negative, false_positive

class ConfusionMatrix(object):
    def __init__(self, X, y, weight=None, tokenize=tokenize_filtered, stop_words=None, len_row=6422, random_state=0):
        self.X = X
        self.y = y
        self.weight = weight
        self.tokenize = tokenize
        self.stop_words = stop_words
        self.len_row = len_row
        self.random_state = random_state

    def svc(self, kernel='rbf', gamma=1):
        model = Pipeline([
        ('vect', CountVectorizer(tokenizer=self.tokenize, stop_words=self.stop_words)),
        ('clf', SVC(kernel=kernel, gamma=gamma))])
        report_list=[]
        recall_list=[]
        precision_list=[]
        f1_list=[]

        cv = ShuffleSplit(self.len_row, random_state=self.random_state)
        for k, (train_index, test_index) in enumerate(cv):
            X_train = self.X[train_index]
            y_train = self.y[train_index]
            X_test = self.X[test_index]
            y_test = self.y[test_index]

            if self.weight != None:
                weight0 = self.weight[train_index]
            else :
                weight0 = None

            model.fit(X_train, y_train, **{'clf__sample_weight' : weight0})
            result = model.predict(X_test)
            report = confusion_matrix(y_test, result)

            if (report[1][0] + report[1][1]) == 0 :
                recall = 'infinite'
            else:
                recall = float(report[1][0]) / (report[1][0] + report[1][1])

            if (report[0][1] + report[1][1]) == 0:
                precision = 'infinite'
            else :
                precision = float(report[1][1]) / (report[1][1] + report[0][1])

            if recall != 'infinite' and precision != 'infinite':
                f1 = 2*recall*precision / float(recall + precision)
            else:
                f1 = 0

            report_list.append(report)
            recall_list.append(recall)
            precision_list.append(precision)
            f1_list.append(f1)
        return report_list, recall_list, precision_list, f1_list

    def multinomial(self, vocabulary=None, ngram=(1,1)):
        model = Pipeline([
        ('vect', CountVectorizer(tokenizer=self.tokenize, vocabulary=vocabulary, stop_words=self.stop_words, ngram_range=ngram)),
        ('clf', MultinomialNB())])
        report_list=[]
        recall_list=[]
        precision_list=[]
        f1_list=[]

        cv = ShuffleSplit(self.len_row, random_state=self.random_state)
        for k, (train_index, test_index) in enumerate(cv):
            X_train = self.X[train_index]
            y_train = self.y[train_index]
            X_test = self.X[test_index]
            y_test = self.y[test_index]

            if self.weight != None:
                weight0 = self.weight[train_index]
            else :
                weight0 = None

            model.fit(X_train, y_train, **{'clf__sample_weight' : weight0})
            result = model.predict(X_test)

            report = confusion_matrix(y_test, result)
            recall = float(report[1][0]) / (report[1][0] + report[1][1])
            precision = float(report[1][1]) / (report[1][1] + report[0][1])
            f1 = 2*recall*precision / float(recall + precision)

            report_list.append(report)
            recall_list.append(recall)
            precision_list.append(precision)
            f1_list.append(f1)
        return report_list, recall_list, precision_list, f1_list

    def logistic(self, vocabulary=None, ngram=(1,1)):
        model = Pipeline([
        ('vect', CountVectorizer(tokenizer=self.tokenize, vocabulary=vocabulary, stop_words=self.stop_words, ngram_range=ngram)),
        ('clf', SVC(kernel=kernel))])
        report_list=[]
        recall_list=[]
        precision_list=[]
        f1_list=[]

        cv = ShuffleSplit(self.len_row, random_state=self.random_state)
        for k, (train_index, test_index) in enumerate(cv):
            X_train = self.X[train_index]
            y_train = self.y[train_index]
            X_test = self.X[test_index]
            y_test = self.y[test_index]

            if self.weight != None:
                weight0 = self.weight[train_index]
            else :
                weight0 = None

            model.fit(X_train, y_train, **{'clf__sample_weight' : weight0})
            result = model.predict(X_test)

            report = confusion_matrix(y_test, result)
            recall = float(report[1][0]) / (report[1][0] + report[1][1])
            precision = float(report[1][1]) / (report[1][1] + report[0][1])
            f1 = 2*recall*precision / float(recall + precision)

            report_list.append(report)
            recall_list.append(recall)
            precision_list.append(precision)
            f1_list.append(f1)
        return report_list, recall_list, precision_list, f1_list
