#!/usr/bin/env python
# encoding: utf=8

import echonest.audio as audio
from dsp import *

PATH = "/Users/grav/Desktop/"
INPUT = PATH+ "stravinsky.m4a"
MAX_CHUNKS = 20
# WINDOW = np.blackman(chunk)

def saveChunk(audioFile,chunk,chunkId):
    audioChunk = audio.getpieces(audioFile,[chunk])
    tmpFile = PATH + "chunks/chunk_"+"%03d" %chunkId +".wav"
    audioChunk.encode(tmpFile)

def saveChunks(audioFile):
    chunks = audioFile.analysis.segments
    n = min(MAX_CHUNKS ,len(chunks))

    for i in range(0,n):
        print "writing %d of %d" % (i+1,n)
        saveChunk(audioFile,chunks[i],i)


def analyze(audioFile,chunk):
    d=DSP(audioFile,chunk)
    d.apply()
    return d.chunk

peakScore = {}

# 
audioFile = audio.LocalAudioFile(INPUT)
chunks = audioFile.analysis.segments
superChunks = audio.AudioQuantumList(map(lambda c: analyze(audioFile,c), chunks))


