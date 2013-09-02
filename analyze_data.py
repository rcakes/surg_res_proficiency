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
    # Extract the database connection info from the configuration info.
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
    # counts = count_resident_cases(cases)
    count_resident_cases(db)


def count_resident_cases(db):
    """
    Count the resident cases.

    :param db: database object
    :type db:  Database class
    :return:
    :rtype:
    """
    # res_cols = [1, 2]
    # res_names = [make_resident_name(case[2], case[1]) for case in cases]
    # c = Counter(res_names)
    # print 'Resident\tCase count'
    # for res, count in c.most_common():
    #     print res + '\t' + str(count)

    # Define the CPT code groups by operation type.
    cpt_groups = {
        'appy': [44970, 44950, 44960],
        'open_colectomy': [44140, 44141, 44143, 44144, 44145, 44146, 44150, 44151, 44155, 44156, 44160],
        'lap_colectomy': [44204, 44206, 44207, 44208, 44211, 44212],
        'lap_choley': [47562, 47563, 47600, 47605],
        'open_inguinal_hernia': [49505, 49507, 49520, 49521, 49525],
        'lap_inguinal_hernia': [49650, 49651]
    }
    # for group_name, cpt_codes in cpt_groups.iteritems():
    #     # Query for the number of cases in the current CPT group.
    #     results = db.count_cpt_group_by_resident(cpt_codes)
    #     for result in results:
    #         res_first_name, res_last_name, num_cases = result
    #         print group_name, res_first_name, res_last_name, num_cases
    # Do the same query, but by pgy this time.
    print '\t'.join(['CPT group', 'First name', 'Last name', 'PGY', 'Num cases'])
    for group_name, cpt_codes in cpt_groups.iteritems():
        # Query for the number of cases in the current CPT group.
        results = db.count_cpt_group_by_resident(cpt_codes, by_pgy=True)
        for result in results:
            res_first_name, res_last_name, pgy, num_cases = result
            print '\t'.join([group_name, res_first_name, res_last_name, str(pgy), str(num_cases)])

    # return c


def make_resident_name(first, last):
    """
    Combine the resident name parts to make the full name.

    :param first: resident's first name
    :type first: str
    :param last: resident's last name
    :type last: str
    :return: resident's full name
    :rtype: str
    """
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
