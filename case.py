from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()

class Case(Base):
    """ This class represents a surgical case. """

    __tablename__ = 'cases'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    type = Column(String)

