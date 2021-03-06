# -*- coding: utf-8 -*-
# @Author: chandan
# @Date:   2017-07-08 00:32:24
# @Last Modified by:   chandan
# @Last Modified time: 2017-07-08 11:14:04

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.models import load_model

from sklearn.preprocessing import MinMaxScaler

from config import MODEL_DIR, SCORE_COLUMNS

import os.path as osp

def build_model():
	# create and fit the LSTM network
	model = Sequential()
	model.add(LSTM(4, input_shape=(16, 28)))
	model.add(Dense(len(SCORE_COLUMNS)))
	model.compile(loss='mean_squared_error', optimizer='adam')

	return model

def train_model(X, Y):
	model = build_model()
	model.fit(X, Y, epochs=100, validation_split=0.2)
	model.save(osp.join(MODEL_DIR, 'lstm.h5'))

def test_model(X, Y):
	model = load_model(osp.join(MODEL_DIR, 'lstm.h5'))
	loss = model.evaluate(X, Y)

	return loss
