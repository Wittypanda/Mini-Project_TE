import librosa
import numpy as np
import os

mel_signals = []
labels = []

di = 'archive'
def generate_mel_signals(directory):
    # Define the frequency ranges for each mood
    mood_ranges = {'depression': (10, 75),
                   'sadness': (75, 150),
                   'anticipation': (150, 300),
                   'joy': (300, 500),
                   'enlightenment': (500, 700)}
    
    
    # Loop through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".wav"):
            file_path = os.path.join(directory, filename)
            # Load the audio file using librosa
            y, sr = librosa.load(file_path)
            # Compute the Mel spectrogram
            S = librosa.feature.melspectrogram(y=y, sr=sr)
            # Convert to decibels
            S_dB = librosa.power_to_db(S, ref=np.max)
            # Flatten the spectrogram into a 1D array
            flat_S = S_dB.flatten()
            # Determine the label for the file based on the frequency range
            label = None
            for mood, freq_range in mood_ranges.items():
                if freq_range[0] <= librosa.mel_frequencies()[0] and freq_range[1] >= librosa.mel_frequencies()[-1]:
                    label = mood
                    break
            if label is not None:
                mel_signals.append(flat_S)
                labels.append(label)

    return np.array(mel_signals), np.array(labels)

    
generate_mel_signals(di)
print(mel_signals)
print(labels)

