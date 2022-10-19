from scipy.io import wavfile
import sys
from recognize import to_text

# https://newscatcherapi.com/blog/ultimate-guide-to-text-similarity-with-python
def jaccard_similarity(x,y):
  """ returns the jaccard similarity between two lists """
  intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
  union_cardinality = len(set.union(*[set(x), set(y)]))
  return intersection_cardinality/float(union_cardinality)

def get_rate(first_path, second_path):
    first_text = to_text(first_path).lower().split(" ")
    second_text = to_text(second_path).lower().split(" ")
    score = jaccard_similarity(first_text, second_text)
    print(f'Similarity score: {score}\n')

if __name__ == 'main':
    first_path = sys.argv[1]
    second_path = sys.argv[2]
    get_rate(first_path, second_path)

