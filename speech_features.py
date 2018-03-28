import numpy as np
from python_speech_features import mfcc


def filtering(samples, sample_rate):
    return samples


def preprocess(samples, sample_rate):
    return samples


def features(samples, sample_rate):
    # фильтрация
    samples = filtering(samples, sample_rate)

    # предобработка
    samples = preprocess(samples, sample_rate)

    # расчёт признаков
    coefs = mfcc(samples)
    
    return np.concatenate((np.mean(coefs, axis=0), np.var(coefs, axis=0)))
    # return np.random.normal(0, 1, 13)
