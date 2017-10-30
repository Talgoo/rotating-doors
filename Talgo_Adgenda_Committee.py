# -- coding: utf-8 --
import csv
import glob2
import os
from collections import defaultdict
from collections import namedtuple

# CONSTS
protocol_dir = os.path.dirname(os.path.abspath(__file__))+"/**/*.csv"

base_values = ["committee", "committee_date", "agenda"]



def handle_files():
    '''
    The main function to start processing the files
    the function should be run (by default) with
    :return: peoples, errors
    '''
    peoples, errors = [], []
    file_prefix = "/committee_"
    for file_name in glob2.glob(protocol_dir):
        if file_prefix in file_name:
            _, partial_path = file_name.split(file_prefix)
            committee_name, raw_date, _ = partial_path.split("/")
            committee_name = raw_date.split("_")[0]
            committee_date = raw_date.split("_")[1]
            people = extract_adgenda(file_name, committee_name, committee_date)
            peoples.extend(people)
    return peoples

def extract_adgenda(file_name, committee, committee_date):
    """

    :param file_name: the file we are working on
    :param committee: the comititee name
    :param committee_date: the date the comitee took place
    :return: list of peoples, list of comittee_names that could not be parsed
    """
    agendas = []
    with open(file_name) as f:
        reader = csv.DictReader(f)
        for row in reader:
            clean_data = row["header"].strip()
            if "סדר היום" in clean_data:
                agendas.append(
                    {'agenda': row["body"].strip(),
                     'committee':committee,
                     'committee_date':committee_date})
    return agendas


def write_to_files(agendas):
        with open('agendas_committees.csv', 'w') as f:
            w = csv.DictWriter(f, agendas[0].keys())
            w.writeheader()
            for agenda in agendas:
                w.writerow(agenda)



def main():
    agendas = handle_files()
    write_to_files(agendas)
    pass


if __name__ == '__main__':
    main()