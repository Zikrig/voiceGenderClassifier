# Задача: 
# Для каждой аудиозаписи:
# Получить спектрограмму
# Поделить на кусочки одинаковой длины - оптимальный размер предстоит выяснить
# Если общая длина меньше максимального то последний кусок дополнить пробелами
# Иначе вырезать кусок, перекрывая предыдущий
# Сохранить как датасет
# использовать объект rca для уменьшения числа переменных
import os
import librosa
import numpy as np
import pandas as pd

class MakeDataset:
    def __init__(self, folderToCut, filesList, folderForFinal):
        self.folderToCut = folderToCut
        self.filesList = filesList
        self.folderForFinal = folderForFinal
        
        if(self.folderToCut[-1] != '\\'):
            self.folderToCut += "\\"
        if(self.folderForFinal[-1] != '\\'):
            self.folderForFinal += "\\"

        if(not os.path.exists(self.folderForFinal)):
            os.mkdir(self.folderForFinal)

    def cutAll(self, lenOfTact, mx=100000):
        # files = os.listdir(self.folderToCut)
        i = 0

        finSpectrList = []
        finSexList = []
        # avg_pool_2d = lay.AveragePooling2D(pool_size=(100, 100), strides=(1, 1), padding='same')

        with open(self.filesList, 'r') as targ:
            for ln in targ:
                audioName, sex = ln.split('\t')
                sex = sex.replace('\n','')
                pathToAudio = self.folderToCut+audioName+'.wav'
                if(not os.path.exists(pathToAudio)):
                    i += 1
                    continue
                y, sr = librosa.load(pathToAudio)
                spectr = librosa.feature.melspectrogram(y=y, sr=sr).T
                # spOb = tf.reshape(spectr, [1, len(spectr), len(spectr[0]), 1])
                # print(spOb.shape)
                # cropped = spOb
                # print(cropped)

                finSpectrList.append(spectr.reshape(-1))
                finSexList.append(sex)

        # df = pd.DataFrame({
        #     'spectr': finSpectrList,
        #     'sex': finSexList
        # })
        # print(finSpectrList.shape)
        cols = [fr"spectr_{jj}" for jj in range(len(finSpectrList))]
        df = pd.DataFrame(finSpectrList, columns=cols)
        print("Датафрейм успешно создан")
        df.insert(0,'sex', finSexList)
        print("Добавили столбец в датафрейм")
        df.to_csv(self.folderForFinal+f"dataset_{lenOfTact}_{mx}.scv", index=False, chunksize=250)
        print("Сохранили датафрейм")
        return df
    
