# Author: INT3R-N3T
# Date created: 7/16/2021

# Welcome to kera
# This is the brain of the project where I will be sticking most of the code
# Hope you enjoy this little project (for more information see the README or the Github page)
# PS: I am too lazy to make proper documentation so if someone besides me gets this code have fun!!

import speech_recognition as sr


#Iniciate Speech Regognizer
r = sr.Recognizer()


#Takes audiofile and records it to audio file (it is an AudioData instance now)
harvard = sr.AudioFile('audio_files_harvard.wav')

with harvard as source:

    # the duration ajusts the testing phase to understand the background noise
    # In further development we could use SciPy to preprocess the audio
    #r.adjust_for_ambient_noise(source, duration=0.5)

    audio = r.record(source)


#Meathod that uses google API to recognize the speech
#There are duration arguments depending on how much of the audio you want to parce, same thing with record it has a duration as well
speech = r.recognize_google(audio)

print(speech)

#NEXT DAY HEY LOOOOOK OVER HERE LOOK OVER HERE DO PIP INSTALL PYAUDIO------------------------------------------------------------------------------------