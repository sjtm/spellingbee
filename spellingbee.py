#!/usr/bin/python

import sys

words = open("words.txt").read().splitlines()

valid_words = []
required_letter = sys.argv[1][0]
letters = set(sys.argv[1])

for word in words:
  word_letters = set(word)
  if (len(word) > 3
      and required_letter in word_letters
      and word_letters.issubset(letters)):
    valid_words.append(word)

for i in sorted(valid_words, key=lambda w: -len(w)):
  print i
