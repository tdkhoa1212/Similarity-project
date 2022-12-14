# Similarity-project
## 1. Guideline

    1. Read Description/Case 2 
    2. Read Description/Input constraints for case 2 
    3. Read Run commands/Case 2/Tone output 
## 2. Description
### 2.1. Case 1
- In the phase 1: Audio files are converted to texts
    - Example: apple_and_lemon.wav transformed to "apple and lemon"
- In the phase 2: Jaccard similarity method is used to score the similarity between two texts
(https://newscatcherapi.com/blog/ultimate-guide-to-text-similarity-with-python)
    - Example: ![alt text](https://github.com/tdkhoa1212/Similarity-project/blob/main/images/matric.png)

### 2.2. Case 2
![alt text](https://github.com/tdkhoa1212/Similarity-project/blob/main/images/case_2.png)

### 2.3. Input constraints for case 2
#### 2.3.1. Train data: 
**Path:** \
./wav/train_wav/ \
**Constraint:** \
    - Only one certain Frequency \
    - Amplitude: 0.8 \
    - Length: > 1s 



#### 2.3.2. Test data:
**Path:** \
./wav/test_wav/ \
**Constraint:**  \
    - Any frequencies in train data \
    - Amplitude: Any \
    - Length of tones: Any \
    - Length of silence: More than cutting_time in Parameter (can be 0.2) 


## 3. Run commands
    pip install -r requirements.txt

### 3.1. Case 1
    %cd Similarity-project/case_1
    python similar_rate.py "the first .wav file path" "the second .wav file path"

### 3.2. Case 2
**Plot spectrogram**

    %cd Similarity-project/case_2
    python plot_extraction.py "the first .wav file path" "the second .wav file path" "the saving path of the demonstration photo"

**Tone output**

    %cd Similarity-project/case_2
    python main.py ./train_wav ./test_wav/"test file" 0.2

***./train_wav:*** Direction of the .wav train folder \
***./test_wav/"test file":*** Direction of a .wav test file \
***0.2:*** Time of cut segments in test audio 

