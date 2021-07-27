import os

from ear import *
from mouth import *


# this takes voice from ear and converts it into string
listen = Voicetotext(mic, r)

speak(listen)