import numpy as np
from sklearn.decomposition import PCA
from scipy.io import wavfile
import matplotlib.pyplot as plt
from ssqueezepy import ssq_cwt
from scipy import signal

def spectrogram(filename):
    '''
    convert raw audio to spectrogram
    '''
    sample_rate, x = wavfile.read(filename) 
    Twx, Wx, *_ = ssq_cwt(x) 
    x_out = abs(Wx)
    print(x_out.shape)
    return x_out
    
def PCA_transform(filename):
    # transform the vector to a matric
    x = spectrogram(filename)
    print(f'Spectrogram (Twx)shape: {x.shape}\n')

    # reduce dimension of matric by PCA
    pca = PCA(n_components=1, svd_solver='arpack')
    y = np.squeeze(pca.fit_transform(x))
    return y
    