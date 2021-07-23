import pyttsx3

#initilise the language engine
engine = pyttsx3.init()



"""-----------------------------Custimise Voice--------------------------

#will change rate of speech

rate = engine.getProperty('rate')
engine.setProperty('rate', rate+50)

#will change voice

engine.setProperty('voice', voice.id)

#will find voices

voices = engine.getProperty('voices') 

for voice in voices:
    if 'en_US' in voice.languages or 'en_GB' in voice.languages:
        print(voice.id)


#NOTE: need to find voices that work on the pie or whatever system cause voice right now is not cool

----------------------------------------------------------------------"""

#speech cmd
engine.say("I love, python")
engine.say("it is pretty cool")

#end speech with
engine.runAndWait()




