# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
from scipy.stats import skew
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import make_scorer, mean_squared_error
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor

def preprocess(train, test):
    y_train = train.SalePrice
    train.drop(['Id','SalePrice'], axis=1, inplace=True)
    test.drop(['Id'], axis=1, inplace=True)

    # null 값이 많은 feature 삭제
    missing = train.isnull().sum()
    to_delete = missing[missing>600]
    train.drop(list(to_delete.index), axis=1, inplace=True)
    test.drop(list(to_delete.index), axis=1, inplace=True)

    category = train.dtypes[train.dtypes=='object'].index
    numerical = train.dtypes[train.dtypes!='object'].index

    #skewed 된 자료를 log를 취해준다.
    skewness = train[numerical].apply(lambda x : skew(x.dropna()))
    skew_idx = skewness[skewness>0.75].index
    train[skew_idx]=np.log1p(train[skew_idx])
    test[skew_idx]=np.log1p(test[skew_idx])

    #categorical data의 null 값을 최빈값으로 채운다.
    for i in category:
        train[i].fillna(train[i].mode().values[0], inplace=True)
        test[i].fillna(test[i].mode().values[0], inplace=True)

    #numerical data의 null 값을 중앙값으로 채운다.
    for i in numerical:
        train[i].fillna(train[i].median(), inplace=True)
        test[i].fillna(test[i].median(), inplace=True)

    #categorical 변수 인코딩
    train = pd.get_dummies(train)
    test = pd.get_dummies(test)

    dif = []
    for i in train.columns:
        if i not in test.columns:
            dif.append(i)

    test_null0 = np.zeros((1459,16))
    test_null = pd.DataFrame(test_null0, columns=dif)
    test = pd.concat([test, test_null], axis=1)    

    X_train = train
    X_test = test
    y_train = np.log1p(y_train)

    return X_train, X_test, y_train

def error(real_value, prediction):
    return mean_squared_error(real_value,prediction)**0.5

RMSE = make_scorer(error, greater_is_better=False)

def random_forest(X_train, X_test, y_train):
    rfr = RandomForestRegressor(random_state=0)
    param_grid = {'n_estimators':[600,700], 'max_features':[20,25,30], 'max_depth':[9,11,13]}
    model = GridSearchCV(estimator=rfr, param_grid=param_grid, n_jobs=2, cv=10, scoring=RMSE)
    model.fit(X_train, y_train)

    print 'best score:'
    print model.best_score_
    print
    print 'best params:'
    print model.best_params_

    return model.best_score_, model.best_params_, model.grid_scores_

def gradient_boost(X_train, X_test, y_train):
    gbr = GradientBoostingRegressor(random_state=0)
    param_grid = {'n_estimators': [1300,1500,1700],'max_features': [13],'max_depth': [3],'learning_rate': [0.05]}
    model = GridSearchCV(estimator=gbr, param_grid=param_grid, n_jobs=2, cv=8, scoring=RMSE)
    model.fit(X_train, y_train)
    print 'best score:'
    print model.best_score_
    print
    print 'best params:'
    print model.best_params_

def gradient_boosting0(X_train, X_test, y_train):
    gbr = GradientBoostingRegressor(random_state=0)
    param_grid = {'n_estimators': [500],'max_features': [10,15],'max_depth': [6,8,10],'learning_rate': [0.05,0.1,0.15],'subsample': [0.8]}
    model = GridSearchCV(estimator=gbr, param_grid=param_grid, n_jobs=1, cv=10, scoring=RMSE)
    model.fit(X_train, y_train)
    print 'best score:'
    print model.best_score_
    print
    print 'best params:'
    print model.best_params_
    y_pred = model.predict(X_test)
    return np.exp(y_pred)

def extra_trees(X_train, X_test, y_train):
    etr=ExtraTreesRegressor(random_state=0)
    param_grid = {'n_estimators': [900,1000,1100], 'max_depth':[20,40,60,80], 'max_features': [80,100,120,140]}
    model = GridSearchCV(estimator=etr, param_grid=param_grid, n_jobs=2, cv=8, scoring=RMSE)
    model.fit(X_train, y_train)
    print 'best score:'
    print model.best_score_
    print
    print 'best params:'
    print model.best_params_

train=pd.read_csv('./data/train.csv')
test=pd.read_csv('./data/train.csv')

X_train, X_test, y_train = preprocess(train,test)
best_score, best_params, all_scores = extra_trees(X_train, X_test, y_train)
