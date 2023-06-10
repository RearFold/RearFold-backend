from sqlalchemy import Column, ForeignKey
from sqlalchemy import VARCHAR, Integer, String, Text, TIMESTAMP
from sqlalchemy.orm import relationship

from member.database import Base

class UserAccount(Base):
    __tablename__ = "user_account"
    email = Column(Integer, primary_key=True)
    pw = Column(String, nullable=False)
    name = Column(String)
    # fullname = Column(String)
    # addresses = relationship(
    #     "Address", back_populates="user", cascade="all, delete-orphan"
    # )
    def __repr__(self):
        return f"User(email={self.email!r}, pw={self.pw!r}, name={self.name!r})"

# class Address(Base):
#     __tablename__ = "address"
#     id = Column(Integer, primary_key=True)
#     email_address = Column(String, nullable=False)
#     user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
#     user = relationship("User", back_populates="addresses")
#     def __repr__(self):
#         return f"Address(id={self.id!r}, email_address={self.email_address!r})"

class Admin(Base):
    __tablename__ = 'admin'
    admin_id = Column(VARCHAR(80), primary_key=True)
    admin_pw = Column(VARCHAR(200), nullable=False)
    created_at = Column(TIMESTAMP)
    description = Column(Text)