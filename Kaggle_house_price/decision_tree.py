# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
from scipy.stats import skew
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import make_scorer, mean_squared_error
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor

def preprocess(train, test):
    all_data = pd.concat([train.loc[:,'MSSubClass':'SaleCondition'], test.loc[:,'MSSubClass':'SaleCondition']])

    to_delete = ['Alley','FireplaceQu','PoolQC','Fence','MiscFeature']
    all_data.drop(to_delete, axis=1, inplace = True)

    #log transform
    numeric_feats = all_data.dtypes[all_data.dtypes != "object"].index
    skewness = all_data[numeric_feats].apply(lambda x : skew(x.dropna()))
    skewed_feats = skewness[skewness>0.75].index
    all_data[skewed_feats] = np.log1p(all_data[skewed_feats])

    #encode categorical data
    all_data=pd.get_dummies(all_data)

    #fillna
    all_data = all_data.fillna(all_data.mean())

    X_train = all_data[:train.shape[0]]
    X_test = all_data[train.shape[0]:]
    y_train = np.log1p(train.SalePrice)

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

def extra_trees(X_train, X_test, y_train):
    etr=ExtraTreesRegressor(random_state=0)
    param_grid = {'n_estimators': [1000,1050,1100,1200], 'max_depth':[10,20,30,40], 'max_features': [150,160,180,200]}
    model = GridSearchCV(estimator=etr, param_grid=param_grid, n_jobs=1, cv=5, scoring=RMSE)
    model.fit(X_train, y_train)
    print 'best score:'
    print model.best_score_
    print
    print 'best params:'
    print model.best_params_

def svr(X_train, X_test, y_train):
    svr = SVR()
    param_grid = {'C':[7,10,13,15], 'gamma':[0.000001, 0.00001, 0.00005, 0.0001] }
    model = GridSearchCV(estimator=svr, param_grid=param_grid, cv=5, scoring=RMSE)
    model.fit(X_train, y_train)
    print model.best_score_
    print model.best_prams_

df_train=pd.read_csv('./data/train.csv')
df_test=pd.read_csv('./data/train.csv')

X_train, X_test, y_train = preprocess(df_train,df_test)
extra_trees(X_train, X_test, y_train)
