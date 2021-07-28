"""
My goals for the brain is that it will be able to sit and wait for a hello cmd.
then i want it to give a greeting. after that it will listen for cmd words. 
and then use other moduels to follow through with that cmd.

"""






import os
import time
import json

from ear import *
from mouth import *




while True:


    # this takes voice from ear and converts it into string
    greetingRequest = Voicetotext(mic, r)

    # This if trys to find hello and key
    if (greetingRequest.find("hello") != -1) & (greetingRequest.find("Kira") != -1):
        
        # will speak the greeting
        speak("Hey Dom, how are you today")
        break
    else:
        time.sleep(1)
        continue



