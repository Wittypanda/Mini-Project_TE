
import librosa
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score


# print('shree ganeshay namaha !!!')
lb = LabelEncoder()

df = []
mfc = []
# map = {
#     "Depression": range(10,75),
#     "Sadness": range(75,150),
#     "Anticipation" : range(150,310),
#     "Joy" : range(310,500),
#     "Enlightment" : range(500,700)
# }

# lr = LinearRegression(**map)
# af = lr.set_params(**map)
# print(af)


dff = pd.read_csv('C:/Users/hp/Documents/mapping.csv')
x = dff.drop("frequency",axis=1)
g = pd.cut(dff["frequency"],5, labels=['Depression','Sadness','Anticipation','Joy','Enlightment'])
lb.fit(g)
y = lb.transform(g)
# print(y)


for i in range(1,9):
    n = i
    f = str(n)
    sig, fs = librosa.load('C://Users//hp//Desktop//Adi_college//Mini Project_TE//archive//'+(f)+'.wav')
    S = librosa.feature.melspectrogram(y=sig, sr=fs)
    df.append(S)
    a,b = librosa.load('C://Users//hp//Desktop//Adi_college//Mini Project_TE//archive//'+(f)+'.wav',res_type='kaiser_fast')
    mfcss = np.mean(librosa.feature.mfcc(y=a,sr=b,n_mfcc=40).T,axis=0)
    mfc.append(mfcss)

print('\ndone\n')
print(df)
print(mfc)

x = tuple(mfc)
# print(x.shape())
y = tuple(df)
# print(y.shape())


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=42) 

knn = KNeighborsClassifier(n_neighbors=50)
knn.fit(x_train,y_train)

x_pred = knn.predict(y_train)
y_pred = knn.predict(y_test)

print('K-Nearest Neighbor')
print('Test Accuracy Score: ', accuracy_score(y_pred, y_test)*100)
print('Test Recall Score: ', recall_score(y_test, y_pred, average='micro')*100)
print('Test F1 Score: ', f1_score(y_test, y_pred, average='micro')*100)
