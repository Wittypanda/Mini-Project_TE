import librosa
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

df = []
mfc = []

for i in range(1,8):
    n = i
    f = str(n)
    sig, fs = librosa.load('C://Users//hp//Desktop//Adi_college//Mini Project_TE//archive//'+(f)+'.wav')
    S = librosa.feature.melspectrogram(y=sig, sr=fs,n_fft=64,n_mels=64)
    df.append(S)
    a,b = librosa.load('C://Users//hp//Desktop//Adi_college//Mini Project_TE//archive//'+(f)+'.wav',res_type='kaiser_fast')
    mfcss = np.mean(librosa.feature.mfcc(y=a,sr=b,n_mfcc=40).T,axis=0)
    mfc.append(mfcss)

print('\ndone\n')
print(df)
# print(mfc)

# from scipy.fftpack import fft

# def mel_to_fft(mel_signal, sample_rate, n_fft=2048, n_mels=128):
#     """
#     Computes the Fourier Transform of a Mel-scaled signal.

#     Args:
#     mel_signal (numpy array): Mel-scaled signal to compute Fourier Transform of
#     sample_rate (int): Sample rate of the signal
#     n_fft (int): Number of FFT points to use (default: 2048)
#     n_mels (int): Number of Mel filter banks to use (default: 128)

#     Returns:
#     numpy array: Fourier Transform of the Mel-scaled signal
#     """

#     # Create Mel filter banks
#     mel_filter = librosa.filters.mel(sample_rate, n_fft, n_mels)

#     # Apply Mel filter banks to signal
#     mel_spectrum = mel_filter.dot(mel_signal)

#     # Compute FFT of Mel spectrum
#     fft_spectrum = np.abs(fft(mel_spectrum, n_fft))

#     return fft_spectrum

# print(mel_to_fft(df,fs))


# def remove_time_frames(data):
#     return data[:, 1:]

# # remove time frames
# data_without_time = remove_time_frames(df)

# # print the result
# print(data_without_time)

# df_mean = [np.mean(t) for t in df]
# # print(df_mean)

# # compute the minimum and maximum values
# min_value = np.min(df_mean)
# max_value = np.max(df_mean)


# # compute the range width and number of intervals
# range_width = (max_value - min_value) / 5
# num_intervals = 5

# # create the range classes
# ranges = [min_value + i * range_width for i in range(num_intervals + 1)]

# # assign values to the range classes
# class_assignments = np.digitize(df_mean, ranges)


# print the range classes and class assignments
# print("Range classes:", ranges)
# print("Class assignments:", class_assignments)


# moods = {'depression': (10, 75),
#                    'sadness': (75, 150),
#                    'anticipation': (150, 300),
#                    'joy': (300, 500),
#                    'enlightenment': (500, 700)}
    

# # Load the mel spectrogram signals and their corresponding labels
# # data = []
# labels = []
# for mood, label in moods.items():
#     for df in range(0,82):
#         df[]
#     df.append()
#     labels.append(label)

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(df, labels, test_size=0.2, random_state=42)

# # Train the machine learning model
# clf = SVC(kernel='linear', C=1.0, probability=True)
# clf.fit(X_train, y_train)

# # Test the machine learning model
# y_pred = clf.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print(f'Accuracy: {accuracy}')

# # Predict the mood of a new mel spectrogram signal
# new_file_path = 'path/to/new/mel/spectrogram/signal'
# new_features = extract_features(new_file_path)
# new_features = np.array(new_features).reshape(1, -1)
# new_mood = list(moods.keys())[clf.predict(new_features)[0]]
# print(f'Predicted mood: {new_mood}')