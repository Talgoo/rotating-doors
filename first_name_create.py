# -- coding: utf-8 --
import requests
import csv
import json
import pprint

# CONSTS
url = 'https://api.dbs.bh.org.il/v1/search?'
total_count = 9985

def requests_first_name(n):
    clean_names = []
    payload = {'collection': 'familyNames', 'from_': str(n), 'q': '*' }
    r = requests.get(url, params=payload)
    j = json.loads(r.text)
    for row in j['hits']['hits']:
        for line in row:
            if line == '_source':
                for leg in row[line]:
                    if leg == 'Header':
                        clean_names.append(row[line][leg].values())
    return clean_names

def write_to_files(clean_names):
    with open('first_name_list.csv', 'w') as f:
        w = csv.writer(f)
        w.writerow(["English", "Hebrew"])  # field header
        w.writerows([list(name) for name in clean_names])

def main():
    clean_names = []
    for i in range(0, total_count, 15):
        clean_names.append(requests_first_name(i))
    write_to_files(clean_names)


if __name__ == '__main__':
    main()
