#!/usr/bin/env python
import sys
import os

from sklearn.feature_extraction import stop_words

stops = set(stop_words.ENGLISH_STOP_WORDS)
# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().lower()
    # remove punctuation
    line = line.translate(None, string.punctuation)
    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
        print '%s\t%s' % (word, "1")
