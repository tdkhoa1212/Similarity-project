import numpy as np
from sklearn.decomposition import PCA
from scipy.io import wavfile
import matplotlib.pyplot as plt
import librosa

def spectrogram(x, sample_rate):
    '''
    convert raw audio to spectrogram using the constant-Q transform
    source: https://librosa.org/doc/main/generated/librosa.cqt.html
    '''
    C = np.abs(librosa.cqt(x, sr=sample_rate, n_bins=60))
    return C
    
def PCA_transform(x, sample_rate):
    # transform the vector to a matric
    C = spectrogram(x, sample_rate)
    # print(f'\nSpectrogram C shape: {C.shape} in (frequency, time)')

    # reduce dimension of matric by PCA
    pca = PCA(n_components=1, svd_solver='arpack')
    y = np.squeeze(pca.fit_transform(C))
    return y
    