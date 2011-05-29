#!/usr/bin/env python
# encoding: utf=8

import echonest.audio as audio
from extraSorting import *
import sys
import os
from dsp import *

INPUT = sys.argv[1]

class Chop:

    def __init__(self,filename):
        self.filename=filename
        self.audioFile = audio.LocalAudioFile(self.filename)
        chunks = self.audioFile.analysis.segments
        print "calculating chunks"
        self.chunks = audio.AudioQuantumList(map(lambda c: self.analyze(c), chunks))

    def saveChunk(self,chunk,chunkId):
        audioChunk = audio.getpieces(audioFile,[chunk])
        dir = self.filename + "_chunks"
        if not os.path.exists(dir):
            os.makedirs(dir)
        tmpFile = dir+"/chunk_" + chunkId +".wav"
        audioChunk.encode(tmpFile)

    def saveChunks(self,chunks,prefix=""):
        n = min(MAX_CHUNKS ,len(chunks))

        for i in range(0,n):
            print "writing %d of %d" % (i+1,n)
            saveChunk(chunks[i],"%s%03d"%(prefix,i))


    def analyze(self,chunk):
        d=DSP(self.audioFile,chunk)
        d.apply()
        return d.chunk

    def output(self,fn,prefix):
        out=audio.getpieces(self.audioFile,self.chunks.ordered_by(fn))
        out.encode(self.filename+"_"+prefix+".wav")



