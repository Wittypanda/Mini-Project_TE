# import numpy as np
# import librosa
# import os
# import sklearn

# # Step 1: Import necessary libraries
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier

# # folder_path = 'archive'
# # Step 2: Define mood frequency classes
# depression = [10, 75]
# sadness = [75, 150]
# anticipation = [150, 300]
# joy = [300, 500]
# enlightenment = [500, 700]

# # Step 3: Define function to generate Mel spectrogram of a WAV file
# def generate_mel_spectrogram(file_path):
#     y, sr = librosa.load(file_path)
#     S = librosa.feature.melspectrogram(y=y, sr=sr)
#     return librosa.power_to_db(S, ref=np.max)

# # Step 4: Define function to generate Mel spectrogram for each file in a folder
# def generate_mel_spectrograms_in_folder(folder_path):
#     mel_spectrograms = []

    
#     for file_name in os.listdir(folder_path):
#         if file_name.endswith('.wav'):
#             file_path = os.path.join(folder_path, file_name)
#             mel_spectrogram = generate_mel_spectrogram(file_path)
#             mel_spectrograms.append(mel_spectrogram)
#     return np.array(mel_spectrograms)

# # Step 5: Define function to classify Mel spectrograms
# def classify_mel_spectrograms(mel_spectrograms):
#     X = mel_spectrograms.reshape(mel_spectrograms.shape[0], -1)
#     y = []
#     for mel_spectrogram in mel_spectrograms:
#         max_freq = np.argmax(np.sum(mel_spectrogram, axis=1))
#         if max_freq >= depression[0] and max_freq <= depression[1]:
#             y.append('depression')
#         elif max_freq >= sadness[0] and max_freq <= sadness[1]:
#             y.append('sadness')
#         elif max_freq >= anticipation[0] and max_freq <= anticipation[1]:
#             y.append('anticipation')
#         elif max_freq >= joy[0] and max_freq <= joy[1]:
#             y.append('joy')
#         elif max_freq >= enlightenment[0] and max_freq <= enlightenment[1]:
#             y.append('enlightenment')
#     return y

# # Step 6: Define function to predict optimal frequencies for a mood
# def predict_optimal_frequencies(mood):
#     if mood == 'depression':
#         return depression
#     elif mood == 'sadness':
#         return sadness
#     elif mood == 'anticipation':
#         return anticipation
#     elif mood == 'joy':
#         return joy
#     elif mood == 'enlightenment':
#         return enlightenment

# # Step 7: Classify Mel spectrograms and output results to file
# mel_spectrograms = generate_mel_spectrograms_in_folder('archive')
# y = classify_mel_spectrograms(mel_spectrograms)
# with open('output_file.txt', 'w') as f:
#     for i in range(len(y)):
#         f.write(f'{i + 1}. {y[i]}\n')

# # Step 8: Predict optimal frequencies for a mood
# mood = 'joy'
# optimal_frequencies = predict_optimal_frequencies(mood)
# print(f'Optimal frequencies for {mood}: {optimal_frequencies}')

