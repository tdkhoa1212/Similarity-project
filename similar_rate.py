from scipy.io import wavfile
import sys
from recognize import to_text

def get_rate(first_path, second_path):
    first_text = to_text(first_path)
    second_text = to_text(second_path)
    

if __name__ == 'main':
    first_path = sys.argv[1]
    second_path = sys.argv[2]
    get_rate(first_path, second_path)

