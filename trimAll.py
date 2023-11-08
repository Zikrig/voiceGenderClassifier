import os
from workWithAudio import *

targetsPath = 'pandModel\\data\\train'
files = os.listdir(targetsPath)
i = 0
for file in files:
    i+=1
    if(i%100 == 0):
        print(i)

    # if(i>20):
    #     break
    newAudio = workWithAudio(targetsPath, file, trimmedPath="pandModel\\data\\trimmedNice\\train")
    newAudio.cutSpaces()
    # newAudio.printSpectrogram()


# targetsPath = 'pandModel\\data\\test'
# files = os.listdir(targetsPath)
# for file in files:
#     newAudio = workWithAudio(targetsPath, file, trimmedPath="pandModel\\data\\trimmedAudio\\test")
#     newAudio.cutSpaces()