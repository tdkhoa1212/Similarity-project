import matplotlib.pyplot as plt
import click
from PCA import PCA_transform

@click.command()
# ******************************Enter your expected information *****************************
@click.option('--filename1', default='/home/ubuntu-pc/Enrico_boss/Similarity-project/wav/Matthew_Male/apple_and_lemon.wav', help='direction of .wav input file')
@click.option('--filename2', default='/home/ubuntu-pc/Enrico_boss/Similarity-project/wav/Matthew_Male/lemon_and_apple.wav', help='direction of .wav input file')
@click.option('--savefile', default='/home/ubuntu-pc/Enrico_boss/Similarity-project/images/new3.png', help='direction of .wav output file')
def plot(filename1, filename2, savefile):
    pca1 = PCA_transform(filename1)
    pca2 = PCA_transform(filename2)
    plt.plot(pca1, label=filename1.split('/')[-1])
    plt.plot(pca2, label=filename2.split('/')[-1])
    plt.legend()
    plt.savefig(savefile)
    plt.show()

if __name__ == '__main__':
    plot()