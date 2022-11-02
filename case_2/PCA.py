import numpy as np
from sklearn.decomposition import PCA
from scipy.io import wavfile
import matplotlib.pyplot as plt
import librosa

def spectrogram(filename):
    '''
    convert raw audio to spectrogram using the constant-Q transform
    source: https://librosa.org/doc/main/generated/librosa.cqt.html
    '''
    # sample_rate, x = wavfile.read(filename) 
    x, sample_rate = librosa.load(filename)
    C = np.abs(librosa.cqt(x, sr=sample_rate, n_bins=60))
    return C, sample_rate
    
def PCA_transform(filename):
    # transform the vector to a matric
    C, sample_rate = spectrogram(filename)
    print(f'\nSpectrogram C shape: {C.shape} in (frequency, time)')

    # reduce dimension of matric by PCA
    pca = PCA(n_components=1, svd_solver='arpack')
    y = np.squeeze(pca.fit_transform(C))
    print(f'PCA shape: {y.shape}\n')
    return y
    