# -- coding: utf-8 --
import csv
import glob2
import os
from collections import defaultdict
from collections import namedtuple
from pyth.plugins.rtf15.reader import Rtf15Reader
from pyth.plugins.plaintext.writer import PlaintextWriter

# CONSTS
protocol_dir = os.path.dirname(os.path.abspath(__file__))+"/**/*.rtf"


def handle_files():
    '''
    The main function to start processing the rtf files
    into csv
    '''
    file_prefix = "\old_committee_"
    for file_name in glob2.glob(protocol_dir):
        if file_prefix in file_name:
            doc = Rtf15Reader.read(open(file_name))
            data = PlaintextWriter.write(doc).getvalue()
            data = data.split(':')
            for leg in data:
                if "מוזמנים" in leg:
                    index_visitor = data.index(leg) + 1
            name = ({'header': 'מוזמנים', 'body': data[index_visitor]})
            dir_file = file_name.replace('.rtf', '.csv')
            with open(dir_file, 'w') as f:
                w = csv.DictWriter(f, name.keys())
                w.writeheader()
                w.writerow(name)
    pass


# def write_to_files(peoples, people_to_jobs_clean):
#     with open('full_people_list.csv', 'w') as f:
#         w = csv.writer(f)
#         w.writerow(base_values)  # field header
#         w.writerows([list(people) for people in peoples])
#
#     with open('person_to_positions.csv', 'w') as f:
#         w = csv.writer(f)
#         w.writerow(["full_name", "positions"])  # field header
#         w.writerows([c for c in people_to_jobs_clean.items()])


def main():
    handle_files()
    # write_to_files(peoples, people_to_jobs_clean)
    pass


if __name__ == '__main__':
    main()