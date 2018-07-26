import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import keras
import numpy as np
import pandas as pd
trainx=pd.read_csv('trainingx.csv')
trainy=pd.read_csv('trainingy.csv')
model=keras.Sequential([
        keras.layers.Dense(100, activation=tf.nn.sigmoid,input_shape=(132,)),
        keras.layers.Dense(70, activation=tf.nn.sigmoid),
        keras.layers.Dense(41, activation=tf.nn.softmax),
        ])
model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(trainx, trainy, epochs=5)
testx=pd.read_csv('testingx.csv')
testy=pd.read_csv('testingy.csv')
model.evaluate(testx,testy)        

