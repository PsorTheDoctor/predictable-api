from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from db import Base


class SubscriberModel(Base):
    __tablename__ = 'subscribers'

    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    enrolling_date = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, email=None):
        self.email = email

    def __repr__(self):
        return '<Subscriber %r>' % self.email
