from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, DECIMAL, func


Base = declarative_base()


class User(Base):
__tablename__ = 'users'
id = Column(Integer, primary_key=True)
username = Column(String(100), unique=True, nullable=False)
password_hash = Column(String(255), nullable=False)
created_at = Column(DateTime, server_default=func.now())


class Order(Base):
__tablename__ = 'orders'
id = Column(Integer, primary_key=True)
user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
product = Column(String(255), nullable=False)
quantity = Column(Integer, nullable=False)
total_price = Column(DECIMAL(10,2), nullable=False)
status = Column(String(50), default='pending')
created_at = Column(DateTime, server_default=func.now())
