from sqlalchemy import Column, Integer, String

from db import Base


class SubscriberModel(Base):
    __tablename__ = 'subscribers'

    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    enrolling_date = Column(String(30))

    def __init__(self, email=None, enrolling_date=None):
        self.email = email
        self.enrolling_date = enrolling_date

    def __repr__(self):
        return '<Subscriber {}>'.format(self.email)
