#!/usr/bin/env python

# Join audio files produced by recorder into one record
# (recorder splits longs sessions into 2Gb+ files)

# * [x] find all WAV files in the current dir
# * [ ] group by size (several files of max size, the last one is smaller)
# * [ ] check metadata that files are from the same chunk
#   * [ ] second file start time should match first file end time
#   * [ ] show metadata diff between files

import os


def get_waves():
    names = os.listdir('.')
    # case insensitive filter for .wav files
    return [n for n in names if n[-4:].lower() == '.wav']


print(get_waves())

