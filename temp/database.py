from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Boolean, Integer, Float, DateTime, Sequence, TIMESTAMP, VARCHAR, Text

db = create_engine('postgresql://hwi:1895@localhost:5432/rearfold',
                   connect_args={'options': '-csearch_path=backend'})
Base =   declarative_base()

Session = sessionmaker(bind=db)
session = Session()

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

# declare model
class User(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)
    addresses = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
    user = relationship("User", back_populates="addresses")
    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

class Admin(Base):
    __tablename__ = 'admin'
    admin_id = Column(VARCHAR(80), primary_key=True)
    admin_pw = Column(VARCHAR(200))
    created_at = Column(TIMESTAMP)
    description = Column(Text)

# auto creation, existed db ok
Base.metadata.create_all(db)

# make select statement

# method 1: module
def add_session(func):
    def wrapper_func(*args, **kwargs):
        try:
            session = Session()
            result = func(session, *args, **kwargs)
            return result
        except:
            pass
        finally:
            session.close()
    return wrapper_func

@add_session
def get_admin_by_id(session, id):
    # select * from admin where admin_id = id
    return session.query(Admin).filter(Admin.admin_id==id)

stmt = get_admin_by_id('root')

# method 2: direct (ORM)
from sqlalchemy import select
stmt = select(Admin).where(Admin.admin_id == 'root')

# execution
rs = session.execute(stmt).fetchall() # returns model object
admin = rs[0][0]  # 첫 번째 튜플의 첫 번째 요소인 Admin 객체에 접근합니다.

admin_id = admin.admin_id
admin_pw = admin.admin_pw
created_at = admin.created_at
description = admin.description

# 데이터 사용
print(admin_id, admin_pw, created_at, description)



from sqlalchemy import insert

# insert method
# stmt = (insert(Admin).values(admin_id='tired', admin_pw='1234'))
# rs = session.execute(stmt)
session.commit()