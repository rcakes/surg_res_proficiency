# system libraries
import numpy as np
import json
from collections import Counter
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy import Column, Integer, String, Date

# project libraries
from resident import Resident
from attending import Attending
from case import Case
from database import Database


def main():
    config = parse_config_file()
    print config
    # Extract the database connection info from the configuation info.
    db_info = config['mysql']
    host = db_info['host']
    user = db_info['user']
    passwd = db_info['passwd']
    db_name = db_info['db_name']
    # create a database object
    db = Database(host, user, passwd, db_name)
    print db.get_num_cases(), 'cases in the database'
    # Calculate the basic stats on the cases.
    calculate_basic_stats(db)


def calculate_basic_stats(db):
    cases = db.get_cases()
    print 'found', len(cases), 'cases'
    print cases[0]
    counts = count_resident_cases(cases)



def count_resident_cases(cases):
    res_cols = [1, 2]
    res_names = [make_resident_name(case[2], case[1]) for case in cases]
    c = Counter(res_names)
    print 'Resident\tCase count'
    for res, count in c.most_common():
        print res + '\t' + str(count)
    return c

def make_resident_name(first, last):
    return first.strip() + ' ' + last.strip()

def count_by_resident(cases, col_nums, res_name_cols=[2, 1]):
    res_names = [make_resident_name(case[res_name_cols[0]], case[res_name_cols[1]])
                 for case in cases]
    c = Counter(res_names)
    print 'Resident\tCase count'
    for res, count in c.most_common():
        print res + '\t' + str(count)
    return c


def parse_config_file(config_file='config.json'):
    """ Parse the configuration file and extract the database info
    :param config_file: the configuration file, in JSON format
    """
    with open(config_file, 'r') as f:
        config = json.load(f)
        return config


if __name__ == '__main__':
    main()
