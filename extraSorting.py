__author__ = 'grav'

"""
basis functions described here
http://developer.echonest.com/docs/v4/_static/AnalyzeDocumentation_2.2.pdf
"""


BRIGHTNESS = 1
ATTACK = 3

def hf(x):
    return x.hf

def lf(x):
    return x.lf

def peak(x):
    return x.peak

def energy(x):
    return x.energy

def kurtosis(x):
    return x.kurtosis

def brightness(x):
    return x.timbre[BRIGHTNESS]

def attack(x):
    return x.timbre[ATTACK]
