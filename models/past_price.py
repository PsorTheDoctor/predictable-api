from sqlalchemy import Column, Integer, String, Numeric

from db import Base


class PastPriceModel(Base):
    __tablename__ = 'past_prices'

    id = Column(Integer, primary_key=True)
    currency = Column(String(50), nullable=False)
    date = Column(String(10), nullable=False)
    value = Column(Numeric, nullable=False)
    # n_days_ago = Column(Integer)

    def __init__(self, currency=None, date=None, value=None):
        self.currency = currency
        self.date = date
        self.value = value

    def __repr__(self):
        return '<Price {} {}>'.format(self.currency, self.date)
