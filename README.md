# Similarity-project
## Plan
![alt text](https://github.com/tdkhoa1212/Similarity-project/blob/main/images/diagram.png)

## Description
- In the phase 1: audio files are converted to texts
    - Example: apple_and_lemon.wav transformed to "apple and lemon"
- In the phase 2: Jaccard similarity method is used to score the similarity between two texts
(https://newscatcherapi.com/blog/ultimate-guide-to-text-similarity-with-python)
    - Example: ![alt text](https://github.com/tdkhoa1212/Similarity-project/blob/main/images/matric.png)

## Run commands
    pip install -r requirements.txt

- Case 1

    %cd Similarity-project/case_1
    python similar_rate.py "the first .wav file path" "the second .wav file path"

- Case 2

    %cd Similarity-project/case_2
    python plot_extraction.py "the first .wav file path" "the second .wav file path" "the saving path of the demonstration photo"

