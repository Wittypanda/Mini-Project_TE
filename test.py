    # _wav_file_ = 'C://Users//hp//Desktop//Adi_college//Mini Project_TE//archive//'+(f)+'.wav'
for i in range(0,2):
    n = i
    f = str(n)
    _wav_file_ = 'C://Users//hp//Desktop//Adi_college//Mini Project_TE//archive//test_adi.wav'


    def mel_sepc_librosa(_wav_file_):
        import librosa
        import numpy as np
        import pylab

        (sigg,rate) = librosa.load(_wav_file_, sr=None, mono=True,  dtype=np.float32)
        print(sigg)
        print(rate)
        pylab.specgram(sigg,Fs=rate)
        pylab.savefig('mel_spectrogram_'+(f)+'.png')

    mel_sepc_librosa(_wav_file_)


#some extrafucntions for similar sort of outputs 

def spectogram_librosa(_wav_file_):
    import librosa
    import pylab
    import numpy as np
    
    (sig, rate) = librosa.load(_wav_file_, sr=None, mono=True,  dtype=np.float32)
    (sigg, rt) = librosa.feature.melspectrogram(_wav_file_, sr = None, mono = True, dtype=np.float32) 
    pylab.specgram(sig, Fs=rate)
    pylab.savefig('mel_spectrogram_67.png')


def graph_spectrogram_wave(wav_file):
    import wave
    import pylab
    def get_wav_info(wav_file):
        wav = wave.open(wav_file, 'r')
        frames = wav.readframes(-1)
        sound_info = pylab.fromstring(frames, 'int16')
        frame_rate = wav.getframerate()
        wav.close()
        return sound_info, frame_rate
    sound_info, frame_rate = get_wav_info(wav_file)
    pylab.figure(num=3, figsize=(10, 6))
    pylab.title('spectrogram pylab with wav_file')
    pylab.specgram(sound_info, Fs=frame_rate)
    pylab.savefig('spectrogram{i}.png')


def graph_wavfileread(_wav_file_):
    import matplotlib.pyplot as plt
    from scipy import signal
    from scipy.io import wavfile
    import numpy as np   
    sample_rate, samples = wavfile.read(_wav_file_)   
    frequencies, times, spectrogram = signal.spectrogram(samples,sample_rate,nfft=1024)
    plt.pcolormesh(times, frequencies, 10*np.log10(spectrogram))
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.savefig("spectogram{i}.png")
    
# spectogram_librosa(_wav_file_)
mel_sepc_librosa(_wav_file_)
#graph_wavfileread(_wav_file_)
#graph_spectrogram_wave(_wav_file_)