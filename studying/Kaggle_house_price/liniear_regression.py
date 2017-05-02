def preprocess(train, test):
    lst_selected =['BsmtFinSF1', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'GarageArea', 'FullBath','GarageCars', 'TotRmsAbvGrd', 'Fireplaces', 'OverallQual',
                   'MSSubClass','MSZoning', 'Neighborhood','MasVnrType', 'ExterQual', 'Foundation','BsmtQual','HeatingQC','KitchenQual', 'GarageType']
    lst_numerical=['BsmtFinSF1', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'GarageArea', 'FullBath','GarageCars', 'TotRmsAbvGrd', 'Fireplaces', 'OverallQual']
    lst_categorical=['MSSubClass','MSZoning', 'Neighborhood','MasVnrType','ExterQual', 'Foundation','BsmtQual','HeatingQC','KitchenQual', 'GarageType']

    df_c = train[lst_selected]
    test = test[lst_selected]

    # 1.MSSubClass : [30,45,180],[50,85,90,160,190],[40,70,75,80],[20,120], [60]
    idx1 = np.where(np.any((df_c['MSSubClass']==30,df_c['MSSubClass']==45,df_c['MSSubClass']==180),axis=0))[0]
    idx2 = np.where(np.any((df_c['MSSubClass']==50,df_c['MSSubClass']==85,df_c['MSSubClass']==90,df_c['MSSubClass']==160,df_c['MSSubClass']==190),axis=0))[0]
    idx3 = np.where(np.any((df_c['MSSubClass']==40,df_c['MSSubClass']==70,df_c['MSSubClass']==75,df_c['MSSubClass']==80),axis=0))[0]
    idx4 = np.where(np.any((df_c['MSSubClass']==20,df_c['MSSubClass']==120),axis=0))[0]
    idx5 = np.where(df_c['MSSubClass']==60)[0]

    df_c.loc[idx1, ['MSSubClass']] = 'idx1'
    df_c.loc[idx2, ['MSSubClass']] = 'idx2'
    df_c.loc[idx3, ['MSSubClass']] = 'idx3'
    df_c.loc[idx4, ['MSSubClass']] = 'idx4'
    df_c.loc[idx5, ['MSSubClass']] = 'idx5'

    idx1 = np.where(np.any((test['MSSubClass']==30,test['MSSubClass']==45,test['MSSubClass']==180),axis=0))[0]
    idx2 = np.where(np.any((test['MSSubClass']==50,test['MSSubClass']==85,test['MSSubClass']==90,test['MSSubClass']==150,test['MSSubClass']==160,test['MSSubClass']==190),axis=0))[0]
    idx3 = np.where(np.any((test['MSSubClass']==40,test['MSSubClass']==70,test['MSSubClass']==75,test['MSSubClass']==80),axis=0))[0]
    idx4 = np.where(np.any((test['MSSubClass']==20,test['MSSubClass']==120),axis=0))[0]
    idx5 = np.where(test['MSSubClass']==60)[0]

    test.loc[idx1, ['MSSubClass']] = 'idx1'
    test.loc[idx2, ['MSSubClass']] = 'idx2'
    test.loc[idx3, ['MSSubClass']] = 'idx3'
    test.loc[idx4, ['MSSubClass']] = 'idx4'
    test.loc[idx5, ['MSSubClass']] = 'idx5'

    # 2.MSZoning : [RM, RH, C (all)]
    idx1 = np.where(np.any((df_c['MSZoning']=='RM', df_c['MSZoning']=='RH', df_c['MSZoning']=='C (all)'), axis=0))[0]
    df_c.loc[idx1, ['MSZoning']] = 'RM'

    idx1 = np.where(np.any((test['MSZoning']=='RM', test['MSZoning']=='RH', test['MSZoning']=='C (all)'), axis=0))[0]
    test.loc[idx1, ['MSZoning']] = 'RM'

    # 3.Neighborhood
    a = ['NAmes','Mitchel','Sawyer','NPkVill','SWISU','Blueste',]
    b = ['OldTown','BrkSide','Edwards', 'IDOTRR','MeadowV','BrDale']
    c = ['CollgCr', 'Crawfor','Somerst','NWAmes', 'Gilbert', 'SawyerW','ClearCr', 'Blmngtn','Veenker','Timber']
    d = ['NoRidge','NridgHt','StoneBr']

    idx_train={}
    idx_test={}
    for i, types in enumerate([a,b,c,d]):
        temp_train=[]
        temp_test=[]
        for t in types:
            idx0 = np.where(df_c['Neighborhood']==t)[0]
            temp_train.extend(idx0)
        for t in types:
            idx0 = np.where(test['Neighborhood']==t)[0]
            temp_test.extend(idx0)
        idx_train['idx{}'.format(i+1)]=temp_train
        idx_test['idx{}'.format(i+1)]=temp_test

    for i in idx_train:
        df_c.loc[idx_train[i],'Neighborhood'] = i
        test.loc[idx_test[i], 'Neighborhood'] = i

    # 4.MasVnrType
    idx = np.where(df_c['MasVnrType']=='BrkCmn')[0]
    df_c.loc[idx,'MasVnrType'] = 'None'

    idx = np.where(test['MasVnrType']=='BrkCmn')[0]
    test.loc[idx,'MasVnrType'] = 'None'

    # 5.Foundation
    idx = np.where(df_c['Foundation']!='PConc')[0]
    df_c.loc[idx,'Foundation'] = 'CBlock'

    idx = np.where(test['Foundation']!='PConc')[0]
    test.loc[idx,'Foundation'] = 'CBlock'

    # 6.HeatingQC
    idx = np.where(df_c['HeatingQC']!='Ex')[0]
    df_c.loc[idx,'HeatingQC'] = 'TA'

    idx = np.where(test['HeatingQC']!='Ex')[0]
    test.loc[idx,'HeatingQC'] = 'TA'

    # 7.GarageType
    idx1 = np.where(np.any((df_c['GarageType']=='BuiltIn', df_c['GarageType']=='Basment', df_c['GarageType']=='2Types'), axis=0))[0]
    idx2 = np.where(df_c['GarageType']=='CarPort')[0]
    df_c.loc[idx1, 'GarageType'] = 'Attchd'
    df_c.loc[idx2, 'GarageType'] = 'Dettchd'

    idx1 = np.where(np.any((test['GarageType']=='BuiltIn', test['GarageType']=='Basment', test['GarageType']=='2Types'), axis=0))[0]
    idx2 = np.where(test['GarageType']=='CarPort')[0]
    test.loc[idx1, 'GarageType'] = 'Attchd'
    test.loc[idx2, 'GarageType'] = 'Dettchd'

    skewness = df_c[lst_numerical].apply(lambda x : skew(x.dropna()))
    skew_idx = skewness[skewness>0.75].index
    df_c[skew_idx] = np.log1p(df_c[skew_idx])
    test[skew_idx] = np.log1p(test[skew_idx])

    null_features = df_c.isnull().sum()[df_c.isnull().sum()!=0].index
    for feat in null_features:
        df_c[feat].fillna(df_c[feat].mode().values[0], inplace=True)

    for feat in lst_numerical:
        test[feat].fillna(test[feat].median(), inplace=True)
    for feat in lst_categorical:
        test[feat].fillna(test[feat].mode().values[0], inplace=True)

    X_train=pd.get_dummies(df_c)
    X_test=pd.get_dummies(test)

    y_train=np.log1p(train.SalePrice)

    return X_train, X_test, y_train

#backup-----------------
def random_forest(X_train, X_test, y_train):
    rfr = RandomForestRegressor(n_estimators=600,max_features=80,max_depth=19,random_state=0)
    rfr.fit(X_train, y_train)
    y_pred = rfr.predict(X_test)
    return np.exp(y_pred)

def gradient_boosting(X_train, X_test, y_train):
    gbr = GradientBoostingRegressor(n_estimators=1500, max_features=13, max_depth=3, learning_rate=0.05, random_state=0)
    gbr.fit(X_train, y_train)
    y_pred = gbr.predict(X_test)
    return np.exp(y_pred)

def extra_trees(X_train, X_test, y_train):
    etr=ExtraTreesRegressor(random_state=0)
    param_grid = {'n_estimators': [500,600,700], 'max_features': [10,15,20]}
    model = GridSearchCV(estimator=etr, param_grid=param_grid, n_jobs=2, cv=4, scoring=RMSE)
    model.fit(X_train, y_train)
    return np.exp(y_pred)


def elastic_net(X_train, X_test, y_train):
    eln = ElasticNet(l1_ratio=0.5, alpha=0.001, random_state=0).fit(X_train,y_train)
    y_pred = eln.predict(X_test)
    return np.exp(y_pred)
