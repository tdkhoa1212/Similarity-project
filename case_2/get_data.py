import numpy as np
import librosa.display
from PCA import PCA_transform
import os


def get_train_data(train_path):
    all_y = {}
    for i in os.listdir(train_path):
        path = os.path.join(train_path, i)

        # transformed the .wav file train by PCA
        x, sample_rate = librosa.load(path)
        name = path.split('/')[-1]
        y = PCA_transform(x, sample_rate)
        all_y[name] = y

    print('-'*40 + f'\nNumber of train tones: {len(all_y)}\n'+'-'*40)
    return all_y

def get_test_data(test_path, cutting_time):
    # measure time length in points:
    # 11025 -> 0.5s
    # 2205  -> 0.1s

    x, sample_rate = librosa.load(test_path)

    cutting_length = int((cutting_time/0.5)*11025) # cutting length
    batch_num = int(x.shape[0]//cutting_length) # number of segment

    all_y = []
    for i in range(batch_num):
        x_cut = x[i*cutting_length : (i+1)*cutting_length]
        y = PCA_transform(x, sample_rate)
        all_y.append(y.tolist()) # insert all PCA extraction in to a list (y)
    all_y = np.array(all_y)
    return all_y
