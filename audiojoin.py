#!/usr/bin/env python

# Join audio files produced by recorder into one record
# (recorder splits longs sessions into 2Gb+ files)
# gaplessly.

# * [x] find all WAV files in the current dir
# * [ ] group by size (several files of max size, the last one is smaller)
# * [ ] check metadata that files are from the same chunk
#   * [ ] second file start time should match first file end time
#   * [ ] show metadata diff between files

import os
import sys


def get_waves():
    names = os.listdir('.')
    # case insensitive filter for .wav files
    return [n for n in names if n[-4:].lower() == '.wav']

def group(files):
    if len(files) < 2:
        sys.exit('Nothing to join: ' + files)

    ordered = sorted(files)
    group = [ordered.pop()]
    for fname in ordered:
        # * [ ] detect original bitness and make sure it matches
        #   * [ ] ~~preserve bitness if it is not pcm_s16le~~
        # * [ ] encode into FLAC, because WAV/AIFF have 4Gb file limit
        #   * [ ] test that sound is gapless
        # ffmpeg -f concat -i wav.list -ar 48000 lecture.flac
        pass


print(get_waves())

