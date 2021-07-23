# Author: INT3R-N3T
# Date created: 7/16/2021

# Welcome to kera
# This is the brain of the project where I will be sticking most of the code
# Hope you enjoy this little project (for more information see the README or the Github page)
# PS: I am too lazy to make proper documentation so if someone besides me gets this code have fun!!

import speech_recognition as sr



def Voicetotext(mic,r):


    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)


    #Takes audiofile and records it to audio file (it is an AudioData instance now)
    #harvard = sr.AudioFile('audio_files_harvard.wav')

    #with harvard as source:

    # the duration ajusts the testing phase to understand the background noise
    # In further development we could use SciPy to preprocess the audio
    #r.adjust_for_ambient_noise(source, duration=0.5)

    #    audio = r.record(source)


    #Meathod that uses google API to recognize the speech
    #There are duration arguments depending on how much of the audio you want to parce, same thing with record it has a duration as well
    #Need to use try and except blocks cause this returns an UnknownValueError exception

    try:
        speech = r.recognize_google(audio)

    except sr.RequestError:
        speech = "Im sorry there was an error"
    
    except sr.UnknownValueError:
        speech = "I couldn't quite make that out"

    return speech





#Iniciate Speech Regognizer
r = sr.Recognizer()

#Iniciate Microphone
#To iniciate microphone on like a raspberry pieuse list_microphone_names(), then do mic = sr.Microphone(device_index=(whatever index the mic u want is))

mic = sr.Microphone()


if __name__ == "__main__":
    print(Voicetotext(mic, r))


