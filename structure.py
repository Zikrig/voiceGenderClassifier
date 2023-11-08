from workWithAudio import workWithAudio
import os

pathFin = "pandModel\\data\\targets.tsv"

with open(pathFin, "r") as file:
    lines = file.readlines()
    for lnNum in range(len(lines)):
        [name, res] = lines[lnNum].split('\t')
        # print(lnNum, name)

        # Обрезка базовая
        # newAudio = workWithAudio('test', name+'.wav', res=res, trimmedPath="pandModel\\trimmedAudio\\")
        # newAudio.cutSpaces()
        if(not os.path.exists('pandModel\\data\\badAudio\\'+name+'.wav')):
            continue
        newAudio = workWithAudio('pandModel\\data\\badAudio\\', name+'.wav', res=res)
        if(newAudio.audioLen > 2.0):
            os.replace(newAudio.pathFull, 'pandModel\\data\\longAudio\\' + newAudio.name)
        if(newAudio.audioLen < 0.4):
            os.replace(newAudio.pathFull, 'pandModel\\data\\shortAudio\\' + newAudio.name)
        print(newAudio.audioLen)

    file.close()

