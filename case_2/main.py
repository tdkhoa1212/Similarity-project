import numpy as np
from scipy import spatial
import click
from get_data import get_test_data, get_train_data

@click.command()
# ******************************Enter your expected information *****************************
@click.option('--train_path', default='/home/ubuntu-pc/Enrico_boss/Similarity-project/wav/train_wav', help='direction of .wav train file')
@click.option('--test_path', default='/home/ubuntu-pc/Enrico_boss/Similarity-project/wav/test_wav/600_640_700_08.wav', help='direction of .wav test file')
@click.option('--cutting_time', default=0.2, type=float, help='time of cut segments in test audio.')
def compare(train_path, test_path, cutting_time):
    '''
    Comparison using cosine method. 
    The output value is in [0, 1]
    For example:
        0: extremely difference 
        0.2: difference
        0.7: approximately similarity
        1: truly similarity
    '''
    train_data = get_train_data(train_path)
    test_data = get_test_data(test_path, cutting_time)

    output_name = []
    for name in train_data:
        value_train = train_data[name]
        similality = np.array([1-spatial.distance.cosine(i, value_train) for i in test_data]) # similarity between test and train segments 
        # print(name, similality, '\n')
        if True in (similality>0.25):
            output_name.append(name)
    print('='*40 + f'\nOutput: {output_name}\n'+'='*40)

if __name__ == '__main__':
    compare()