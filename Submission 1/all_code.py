# Olah Data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Standarisasi Data
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# K-Nearest Neighbor
from sklearn.neighbors import KNeighborsRegressor
# Random Forest
from sklearn.ensemble import RandomForestRegressor


# Evaluasi
from sklearn.metrics import mean_squared_error

# path dataset obesitas
obesDfPath = 'data/ObesityDataSet_cleaned_and_data_sinthetic.csv'
obesDf = pd.read_csv(obesDfPath)

obesDf.head()

# Cek shape dataset obesitas
obesDf.shape

obesDf.info()

obesDf.isna().sum()

obesDf.duplicated().sum()

obesDf.describe()

obesDf['Weight'] = obesDf.Weight.astype(float)
obesDf.head()

obesDf.info()

# Mengambil hanya kolom yang digunakan
obesDf = obesDf[['Height', 'Weight', 'BMI', 'CAEC', 'NObeyesdad']]

obesDf.head()

# Cek Shape
obesDf.shape
heightZero = (obesDf.Height <= 0).sum()
print(heightZero)

weightZero = (obesDf.Weight <= 0).sum()
print(weightZero)

zeroBMI = (obesDf.BMI <= 0).sum()

print(zeroBMI)

obesDf.shape

sns.boxplot(x=obesDf['Height'])
plt.savefig('assets/height1.png')

sns.boxplot(x=obesDf['Weight'])
plt.savefig('assets/weight1.png')

sns.boxplot(x=obesDf['BMI'])
plt.savefig('assets/BMI1.png')

# Cek shape data awal
obesDf.shape

numerical = obesDf.select_dtypes(include=['float64', 'int64'])
categorical = obesDf.select_dtypes(include=['object'])

# Mengambil kuartil 1 dari keseluruhan data
q1 = numerical.quantile(0.25)
# Mengambil kuartil 3 dari keseluruhan data
q3 = numerical.quantile(0.75)

# Mengurangkan antara kuartil 1 dan 3
iqr = q3 - q1

# Batas atas
upper = q3 + 1.5 * iqr

# Batas bawah
bottom = q1 - 1.5 * iqr

# Rumus outliers
outliers = ((numerical < bottom) | (numerical > upper))

# Data outliers
dataOutliers = obesDf[outliers.any(axis=1)]

dataOutliers
# Cek shape awal
obesDf.shape

# Menambahkan notasi not
cleanedObesDf = obesDf[~outliers.any(axis=1)]
cleanedObesDf.head()

cleanedObesDf.shape

sns.boxplot(x=cleanedObesDf['Weight'])
plt.savefig('assets/weight2.png')

sns.boxplot(x=cleanedObesDf['Height'])
plt.savefig('assets/height2.png')

sns.boxplot(x=cleanedObesDf['BMI'])
plt.savefig('assets/BMI2.png')

cleanedObesDf.Height.max()

numerical = cleanedObesDf.select_dtypes(include=['float64', 'int64'])
categorical = cleanedObesDf.select_dtypes(include=['object'])

# Mengambil kuartil 1 dari keseluruhan data
q1 = numerical.quantile(0.25)
# Mengambil kuartil 3 dari keseluruhan data
q3 = numerical.quantile(0.75)

# Mengurangkan antara kuartil 1 dan 3
iqr = q3 - q1

# Batas atas
upper = q3 + 1.5 * iqr

# Batas bawah
bottom = q1 - 1.5 * iqr

# Rumus outliers
outliers = ((numerical < bottom) | (numerical > upper))

# Data outliers
dataOutliers = cleanedObesDf[outliers.any(axis=1)]

dataOutliers

cleanedObesDf = cleanedObesDf[~outliers.any(axis=1)]

# Cek Shape
cleanedObesDf.shape

# Cek Isi Dataset
cleanedObesDf.head()

# Kolom Numerikal
numFeatures = ['Height', 'Weight', 'BMI']
# Kolom Kategorikal
catFeatures = ['CAEC', 'NObeyesdad']

def featuresExtract(feature):
    count = cleanedObesDf[feature].value_counts()
    percent = 100 * cleanedObesDf[feature].value_counts(normalize=True)   
    df = pd.DataFrame({
        'Jumlah sampel':count, 
        'Persentase':percent.round(1)
        })
    print(df)
    
    rot = 0
    if feature != 'CAEC':
        rot = 45
    count.plot(kind='bar', title='Jumlah Kolom ' + feature, rot=rot)
    

feature = catFeatures[0]
featuresExtract(feature)
plt.savefig('assets/CAEC.png')

feature = catFeatures[1]
featuresExtract(feature)
plt.savefig('assets/nobeyesdad.png')

cleanedObesDf.sample(10)

cleanedObesDf.hist(bins=35, figsize=(18,15))
plt.savefig('assets/numerical.png')
plt.show()

# Mengambil hanya kolom kategorik
catFeatures = cleanedObesDf.select_dtypes(include='object').columns.to_list()

for col in catFeatures:
    sns.catplot(x=col, y='BMI', kind='bar', dodge=False, aspect=3, data=cleanedObesDf, palette='Set3')
    plt.savefig('assets/multi-'+ col +'.png')
    plt.title('Rata-rata BMI Relatif pada Kolom ' + col)
    

sns.pairplot(cleanedObesDf, diag_kind = 'kde')
plt.savefig('assets/multi-numerical-pairplot.png')

colsForMatrix = cleanedObesDf[['Height', 'Weight', 'BMI']]

# Mengambil nilai korelasi
corrMatrix = colsForMatrix.corr().round(2)

# Menggambar Heatmap
plt.figure(figsize=(18, 8))

sns.heatmap(data=corrMatrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.savefig('assets/multi-numerical-heatmap.png')
plt.title("Matriks Korelasi untuk Fitur Numerik", size=20)

# Cek isi dataframe
cleanedObesDf.head()

# Encoding Fitur CAEC
cleanedObesDf = pd.concat([cleanedObesDf, pd.get_dummies(cleanedObesDf['CAEC'], prefix='calories')], axis=1)
# Encoding Fitur NObeyesdad
cleanedObesDf = pd.concat([cleanedObesDf, pd.get_dummies(cleanedObesDf['NObeyesdad'], prefix='obesity')], axis=1)
# Drop fitur asli
cleanedObesDf.drop(['CAEC', 'NObeyesdad'], axis=1, inplace=True)

# Cek isi dataframe
cleanedObesDf.head()

# Fungsi Mengubah True = 1 dan False = 0
def toInt(value):
    if type(value) == bool:
        if value == True:
            return 1
        else:
            return 0
    else:
        return value

cleanedObesDf = cleanedObesDf.applymap(toInt)

cleanedObesDf.head()

# Memastikan relasi dengan pairplot
sns.pairplot(cleanedObesDf[['Height', 'Weight']], plot_kws={'s': 3})
plt.savefig('assets/pca.png')

# Mengambil parameter x
X = cleanedObesDf.drop(['BMI'], axis=1)

# Mengambil parameter y
y = cleanedObesDf['BMI']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.1, random_state=42)


# Cek banyak jumlah X
print('Jumlah banyak data X adalah ', len(X))

# Cek sample isi data
X.sample(5)

# Cek banyak jumlah X_train
print('Jumlah banyak data X_train adalah ', len(X_train))

# Cek sample isi data
X.sample(5)

# Cek banyak jumlah X_test
print('Jumlah banyak data X_test adalah ', len(X_test))

# Cek sample isi data
X.sample(5)

# Mengambil kolom numerik
numericalFeatures = ['Height', 'Weight']
# Mendefinisikan StandarScaler untuk standarisasi
scaler = StandardScaler()
# Melakukan penyesuaian scaller dengan data training di kolom-kolom numerik yang digunakan
scaler.fit(X_train[numericalFeatures])

# Melakukan transformasi pada data
X_train[numericalFeatures] = scaler.transform(X_train.loc[:, numericalFeatures])

# Cek isi sample
X_train[numericalFeatures].sample(20)

X_train[numericalFeatures].describe().round(4)

trainModels = pd.DataFrame(index=['trainMSE', 'testMSE'],
                columns=['KNN', 'RandomForest'])

# Definisikan model
knnModel = KNeighborsRegressor(n_neighbors=5)

# Fitting model
knnModel.fit(X_train, y_train)

# Memasukkan hasil ke dalam wadah hasil
trainModels.loc['trainMSE', 'KNN'] = mean_squared_error(y_pred= knnModel.predict(X_train), y_true=y_train)

# Definisikan model
rfModel = RandomForestRegressor(n_estimators=10, max_depth=4, random_state=25, n_jobs=-1)

# Fitting model
rfModel.fit(X_train, y_train)

# Memasukkan hasil ke dalam wadah hasil
trainModels.loc['trainMSE', 'RandomForest'] = mean_squared_error(y_pred=rfModel.predict(X_train), y_true=y_train)

trainModels.loc['trainMSE', :]

X_test.loc[:, numericalFeatures] = scaler.transform(X_test[numericalFeatures])

X_test[numericalFeatures].sample(10)

trainModels.loc['testMSE', 'KNN'] = mean_squared_error(y_pred=knnModel.predict(X_test), y_true=y_test)

trainModels.loc['testMSE', 'RandomForest'] = mean_squared_error(y_pred=rfModel.predict(X_test), y_true=y_test)

trainModels

fig, ax = plt.subplots()
trainModels.plot(kind='barh', ax=ax)
plt.title('Perbandingan Error dengan MSE')
plt.savefig('assets/compare-error.png')

# Dictionary Model
modelDict = {'KNN': knnModel, 'RF': rfModel}

# Ambil Nilai X dari X_test
XForPredict = X_test[:3].copy()
# Ambil Nilai y asli dari y_test
yForPredict = {'y_true':y_test[:3]}

for name, model in modelDict.items():
    yForPredict['prediksi_'+name] = model.predict(XForPredict).round(1)

pd.DataFrame(yForPredict)