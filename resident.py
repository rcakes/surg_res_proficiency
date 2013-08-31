from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Resident(Base):
    """ This class represents a surgical resident. """

    __tablename__ = 'residents'

    # Define the table columns for the class.
    id = Column(Integer, primary_key=True)
    last_name = Column(String)
    first_name = Column(String)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "<Resident('%s', '%s')>" % (self.first_name, self.last_name)

    def check_data(self):
        """ Check the quality of the data. """
        assert type(self.first_name) is str, 'First name must be a string.'
        assert type(self.lasst_name) is str, 'Last name must be a string.'
        assert self.first_name.strip() != '', 'First name is an empty string.'
        assert self.last_name.strip() != '', 'Last name is an empty string.'
        return True


