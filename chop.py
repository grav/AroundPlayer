#!/usr/bin/env python
# encoding: utf=8

import echonest.audio as audio
import numpy as np

PATH = "/Users/grav/Desktop/"
INPUT = PATH+ "around.mp3"
MAX_CHUNKS = 200
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

def monoSignal(audioFile,chunk):
    audioChunk = audio.getpieces(audioFile,[chunk])
    arr = audioChunk.data
    if arr.ndim==2:
        return arr.mean(1)
    return arr


peakScore = {}

# 
# audioFile = audio.LocalAudioFile(INPUT)
# chunks = _audioFile.analysis.segments

