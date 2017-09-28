# -- coding: utf-8 --
import requests
import csv


# CONSTS
url = 'https://api.dbs.bh.org.il/v1/search?'
total_count = 9985

def requests_first_name(n):
    raw_names = []
    payload = {'collection': 'familyNames', 'from_': str(n), 'q': '*' }
    r = requests.get(url, params=payload)
    for line in r:
        if '"He":' in line:
            raw_names.append(line)
    return raw_names


def main():
    raw_names = []
    for i in range(0, total_count, 15):
        raw_names.append(requests_first_name(i))
        pass



if __name__ == '__main__':
    main()
