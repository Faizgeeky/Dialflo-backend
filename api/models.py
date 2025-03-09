from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey, Float, func
from .database import Base
import enum

#TODO : add more models and normalize it and defin releation ship i.e. users - orderhistory

class QueryTypeEnum(enum.Enum):
    ORDER_STATUS = "order_status"
    NEW_ORDER = "new_order"

from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from enum import Enum as PyEnum

# Enum for query types
class QueryTypeEnum(PyEnum):
    ORDER_STATUS = "order_status"
    NEW_ORDER = "new_order"


class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    phone = Column(String(100), nullable=False, unique=True)

    orders = relationship("OrderHistory", back_populates="user")


class OrderHistory(Base):
    __tablename__ = "orderhistory"
    
    id = Column(Integer, primary_key=True)
    order_id = Column(String, unique=True)
    query = Column(String, nullable=False)
    query_type = Column(Enum(QueryTypeEnum), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    
    # kept nuillable incase if someomes not wiiling to share details can be work with orderid
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    
    # link to user
    user = relationship("Users", back_populates="orders")

    
