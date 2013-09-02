import MySQLdb as mdb


class Database(object):

    def __init__(self, host, user, passwd, db_name):
        """
        :param host: mysql server hostname
        :type host: str
        :param user: mysql user name
        :type user: str
        :param passwd: password
        :type passwd: str
        :param db_name: database name
        :type db_name: str
        """
        self.host = host
        self.user = user
        self.db_name = db_name
        self.con = None
        self.db = None
        # Connect to the mysql database.
        self.connect_to_mysql(self.host, self.user, passwd, self.db_name)

    def __del__(self):
        """ Delete the database object."""
        if self.con is not None:
            self.con.close()

    def connect_to_mysql(self, host, user, passwd, db_name):
        self.con = mdb.connect(host=host, user=user, passwd=passwd, db=db_name)
        self.cur = self.con.cursor()

    def get_num_cases(self, complete=True):
        if complete:
            q = 'select count(*) from cases where overall_val > 0'
        else:
            q = 'select count(*) from cases'
        self.cur.execute(q)
        num_cases = self.cur.fetchone()[0]
        return num_cases

    def get_cases(self, complete=True):
        if complete:
            q = 'select * from cases where overall_val > 0'
        else:
            q = 'select * from cases'
        self.cur.execute(q)
        result = self.cur.fetchall()
        return result

    def count_cases_by_resident(self):
        q = 'select resident_first_name, resident_last_name, count(*) as num_cases from cases group by resident_first_name, resident_last_name order by num_cases desc'
        self.cur.execute(q)
        result = self.cur.fetchall()
        return result

    def count_cpt_by_resident(self):
        q = 'select resident_first_name, resident_last_name, cpt_code, count(cpt_code) as num_cases from cases group by resident_first_name, resident_last_name, cpt_code order by num_cases desc'
        self.cur.execute(q)
        result = self.cur.fetchall()
        return result

    def count_cpt_group_by_resident(self, cpt_group, by_pgy=False):
        """
        :param cpt_group: the cpt codes in the group
        :type cpt_group: list of strings
        :return: database cursor of the query results
        :rtype: mysql database cursor
        """
        # Make sure the collection is a tuple, so that the string version is flanked by parentheses for mysql.
        cpt_group_str = str(tuple(cpt_group))
        # Make the query string.
        if by_pgy:
            # Group by the resident and by PGY.
            q = 'select resident_first_name, resident_last_name, pgy, count(*) as num_cases from cases where cpt_code in ' \
                + cpt_group_str + ' group by resident_first_name, resident_last_name, pgy order by num_cases desc'
        else:
            # Group by the resident.
            q = 'select resident_first_name, resident_last_name, count(*) as num_cases from cases where cpt_code in ' \
                + cpt_group_str + ' group by resident_first_name, resident_last_name order by num_cases desc'
        self.cur.execute(q)
        result = self.cur.fetchall()
        return result
