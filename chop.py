#!/usr/bin/env python
# encoding: utf=8

import echonest.audio as audio
from extraSorting import *
import sys
import os
from dsp import *

INPUT = sys.argv[1]
TYPE = sys.argv[2]
MAX_CHUNKS = 200

class Chop:

    def __init__(self,filename):
        self.filename=filename
        self.audioFile = audio.LocalAudioFile(self.filename)
        if TYPE == 'beats':
            self.chunks = self.audioFile.analysis.beats
        else:
            self.chunks = self.audioFile.analysis.segments
        print "analyzing chunks"

        self.reanalyse()

    def saveChunk(self,chunk,chunkId):
        audioChunk = audio.getpieces(self.audioFile,[chunk])
        dir = self.filename + "_chunks"
        if not os.path.exists(dir):
            os.makedirs(dir)
        filename = dir+"/chunk_" + chunkId +".wav"
        audioChunk.encode(filename)

    def saveChunks(self,fn,prefix,n=8):
        chunks = self.chunks.ordered_by(fn)[-n:]

        n = min(MAX_CHUNKS ,len(chunks))

        for i in range(0,n):
            print "writing %d of %d" % (i+1,n)
            self.saveChunk(chunks[i],"%s_%s%03d"%(TYPE,prefix,i))

    def reanalyse(self):
        self.chunks = audio.AudioQuantumList(map(lambda c: self.analyze(c), self.chunks))


    def analyze(self,chunk):
        d=DSP(self.audioFile,chunk)
        d.apply()
        return d.chunk



    def output(self,fn,prefix):
        out=audio.getpieces(self.audioFile,self.chunks.ordered_by(fn))
        out.encode(self.filename+"_"+prefix+".wav")



