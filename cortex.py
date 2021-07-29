# This is the part of kera that manages non command orented communication
# It uses a chatbot to allow for natural like speech

# Look at https://chatterbot.readthedocs.io/en/stable/ for info on chatterbot

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


keraChat = ChatBot("keraCortex",

    logic_adapters=[
        #Allows for dynamic math and time questions
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter' 


        #read_only=True un comment this to stop learning process
        ]
)


#trainer for the chatbot
trainer = ChatterBotCorpusTrainer(keraChat)

# Train based on the english corpus from the chatterbot github
trainer.train("chatterbot.corpus.english")
trainer.train("chatterbot.corpus.english.greetings")


def getResponce(statement):

    return keraChat.get_response(statement)
