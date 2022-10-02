import os
import matplotlib
matplotlib.use('Agg') # No pictures displayed 
import pylab
import librosa
import librosa.display
import numpy as np

for i in range(1,83):
    n = i
    f = str(n)
        
    sig, fs = librosa.load('C://Users//hp//Desktop//Adi_college//Mini Project_TE//archive//'+(f)+'.wav')   
    # make pictures name 
    save_path = 'test_'+(f)+'.jpg'
    
    pylab.axis('on') # no axis
    # pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[]) # Remove the white edge
    S = librosa.feature.melspectrogram(y=sig, sr=fs)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max),x_axis='time', y_axis='mel')
    pylab.savefig(save_path, bbox_inches=None, pad_inches=0)
    pylab.close()

    # test_'+(f)+'.jpg