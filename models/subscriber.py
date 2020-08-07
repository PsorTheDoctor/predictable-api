from sqlalchemy import Column, Integer, String

from db import Base


class SubscriberModel(Base):
    __tablename__ = 'subscribers'

    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    since = Column(String(30), nullable=False)
    code = Column(Integer)

    def __init__(self, email=None, since=None, code=None):
        self.email = email
        self.since = since
        self.code = code

    def __repr__(self):
        return '<Subscriber {}>'.format(self.email)
