import speech_recognition as sr 

def to_text(path):
    r = sr.Recognizer()
    audio = sr.AudioFile(path)

    with audio as source:
        audio_file = r.record(source)
    try:
        # using google speech recognition
        text = r.recognize_google(audio_file) # text output from the audio file
        print('Converting audio transcripts into text ...\n')
    except:
        print('Sorry.. run again...\n')

    return text