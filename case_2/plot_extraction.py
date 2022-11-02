import matplotlib.pyplot as plt
import click
import numpy as np
import librosa.display
from PCA import spectrogram, PCA_transform

@click.command()
# ******************************Enter your expected information *****************************
@click.option('--filename', default='/home/ubuntu-pc/Enrico_boss/Similarity-project/wav/440hz.wav', help='direction of .wav input file')
@click.option('--savefile', default='/home/ubuntu-pc/Enrico_boss/Similarity-project/images/440hz.png', help='direction of .wav output file')
def plot(filename, savefile):
    # Spectrogram and PCA outputs--------------------------
    C, sample_rate = spectrogram(filename)
    y = PCA_transform(filename)
    print(max(y))

    # Get name---------------------------------------------
    name = filename.split('/')[-1].split('.')[0]

    # plot outputs-----------------------------------------
    fig, ax = plt.subplots(2)
    img = librosa.display.specshow(C, sr=sample_rate, x_axis='time', y_axis='cqt_hz', ax=ax[0])
    ax[0].set_title(f'Constant-Q power spectrum of {name}')
    ax[1].plot(y)
    ax[1].set(xlabel='Frequency resolution', ylabel='Amplitude')
    fig.colorbar(img, ax=ax[0], format="%+2.0f dB")
    fig.savefig(savefile)


if __name__ == '__main__':
    plot()