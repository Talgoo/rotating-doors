# -- coding: utf-8 --
import requests
import json
# import pprint
# import codecs

# CONSTS
url = 'https://api.dbs.bh.org.il/v1/search?'
total_count = 9985
# total_count = 100

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
    with open('first_name_list.csv', 'w') as w:
        # w.write(["English", "Hebrew"])  # field header
        for leg in clean_names:
            for first in leg:
                name = first[1].encode("utf-8")
                w.write(name + '\n')

def main():
    clean_names = []
    for i in range(0, total_count, 15):
        clean_names.append(requests_first_name(i))
    write_to_files(clean_names)
    pass


if __name__ == '__main__':
    main()
