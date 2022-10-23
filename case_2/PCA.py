import numpy as np
from sklearn.decomposition import PCA
from scipy.io import wavfile
import matplotlib.pyplot as plt

def reshape_input(x, nuts=4):
    '''
    reshape vectors to matrices 
    with the shape of (nuts, ...)
    '''
    if x.shape[0]%nuts == 0:
        x_new = x.reshape(nuts, -1)
    else:
        o_length = x.shape[0]
        n_dimension = int(o_length - (o_length%nuts))
        x_new = x.reshape(nuts, n_dimension)
    return x_new 

    
def PCA_transform(filename):
    # get a vector from an audio file
    sample_rate, x = wavfile.read(filename) 

    # transform the vector to a matric
    x_new = reshape_input(x)

    # reduce dimension of matric by PCA
    pca = PCA(n_components=1, svd_solver='arpack')
    y = np.squeeze(pca.fit_transform(x_new))
    return y
    