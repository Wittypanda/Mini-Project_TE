#print("Shree Ganeshay Namah !!!")

#importing 

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

 
import librosa 
import librosa.display
import IPython.display as ipd
import plotly.express as px


pathAudio = "C:/Users/hp/Desktop/Adi_college/Mini Project_TE/archive/"
files = librosa.util.find_files(pathAudio, ext=['wav']) 
files = np.asarray(files)

for y in files: 
    data = librosa.load(y,sr =None,mono=True)   
    # print(data)
df = list(data)
print(type(df[0]))
# fig = px.line(data_frame=df[0])
# fig.show()

for t in df :
    af = pd.Series(df[t])
    fig = px.line(data_frame=af)
    fig.show()

