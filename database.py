import MySQLdb as mdb


class Database(object):

    def __init__(self, host, user, passwd, db_name):
        self.host = host
        self.user = user
        self.db_name = db_name
        self.con = None
        self.db = None
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
            q = 'select count(*) from cases, where overall_value > 0'
        else:
            q = 'select count(*) from cases'
        self.cur.execute(q)
        num_cases = self.cur.fetchone()[0]
        return num_cases

    def get_cases(self, complete=True):
        if complete:
            q = 'select * from cases where overall_value > 0'
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
