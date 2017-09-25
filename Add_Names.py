# -- coding: utf-8 --
import csv
import glob2
import os
from collections import defaultdict
from collections import namedtuple


def main():
    f = open("full_names.csv", 'a')
    raw_more_names = open("T_Translated_Names.txt", "r")
    more_names = []
    for line in raw_more_names:
        __, temp = line.split('(', 1)
        __, temp = temp.split("'", 1)
        temp, __ = temp.split("'", 1)
        more_names.append(temp.strip("'")+'\n')
    f.writelines(more_names)
    f.close()
    raw_more_names.close()
    pass


if __name__ == '__main__':
    main()