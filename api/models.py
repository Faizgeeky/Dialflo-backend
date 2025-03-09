from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey, Float, func
from .database import Base
import enum

#TODO : add more models and normalize it and defin releation ship i.e. users - orderhistory

class QueryTypeEnum(enum.Enum):
    ORDER_STATUS = "order_status"
    NEW_ORDER = "new_order"
    
class OrderHistory(Base):
    __tablename__ = "orderhistory"
    id = Column(Integer, primary_key=True)
    order_id = Column(String, unique=True)
    customer_name = Column(String, unique=False)
    customer_phone = Column(String, unique=False)
    query = Column(String, nullable=False)
    query_type = Column(Enum(QueryTypeEnum), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False) 

    
