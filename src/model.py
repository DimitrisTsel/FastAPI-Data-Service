from sqlalchemy import  Column, Integer, String, Float
from .database import Base

class Item(Base):
    __tablename__ = "data_table"

    index = Column(Integer, primary_key=True)
    InvoiceNo = Column(String, index=True)
    Description = Column(String)
    Quantity = Column(Integer)
    InvoiceDate = Column(String)
    UnitPrice = Column(Float)
    CustomerID = Column(Integer)
    Country = Column(String)

