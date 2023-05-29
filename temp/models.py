from .database import session, base
from sqlalchemy import Column, String, Boolean, Integer, Float, DateTime, Sequence, TIMESTAMP, VARCHAR, Text

class TableName(base):
    __tablename__ = 'test'
    a = Column(String(10), primary_key=True)    # string type, primary key 지정
    b = Column(Integer)                         # Int type
    c = Column(Boolean)                         # Bool type
    d = Column(Float)                           # float type
    e = Column(DateTime)                        # datetime type
    f = Column(Integer, Sequence('table name_id_seq'))   # serial type

class Admin(base):
    __tablename__ = 'admin'
    admin_id = Column(VARCHAR(80), primary_key=True)
    admin_pw = Column(VARCHAR(200))
    created_at = Column(TIMESTAMP)
    description = Column(Text)