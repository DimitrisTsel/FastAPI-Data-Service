from typing import Union

from pydantic import BaseModel

class addRecords(BaseModel):
    InvoiceNo: str
    Description: str
    Quantity: int
    InvoiceDate: str
    UnitPrice: float
    CustomerID: int
    Country: str
