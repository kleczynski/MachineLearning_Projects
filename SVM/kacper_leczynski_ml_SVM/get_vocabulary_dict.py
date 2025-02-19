#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv

from typing import Dict


def get_vocabulary_dict() -> Dict[int, str]:
    """Read the fixed vocabulary list from the datafile and return.

    :return: a dictionary of words mapped to their indexes
    """

    # Parse data from the 'data/vocab.txt' file.
    # - The file is saved in tab-separated values (TSV) format.
    # - Each line contains a word's ID and the word itself.
    # The output dictionary should map word's ID on the word itself, e.g.:
    #   {1: 'aa', 2: 'ab', ...}

    vocabulary_dct = {}
    f = open('data/vocab.txt', 'r')
    lines = csv.reader(f, delimiter='\t')
    for line in lines:
        vocabulary_dct[int(line[0])] = line[1]
    f.close()
    return vocabulary_dct


