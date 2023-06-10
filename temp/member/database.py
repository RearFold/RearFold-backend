import yaml
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine('postgresql://hwi:1895@localhost:5432/rearfold',
                   connect_args={'options': '-csearch_path=backend'})
Base =   declarative_base()

Session = sessionmaker(bind=db)
session = Session()

# # auto creation, existed db ok
# Base.metadata.create_all(db)

# # make select statement

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

# @add_session
# def get_admin_by_id(session, id):
#     # select * from admin where admin_id = id
#     return session.query(Admin).filter(Admin.admin_id==id)

# stmt = get_admin_by_id('root')

# # method 2: direct (ORM)
# from sqlalchemy import select
# stmt = select(Admin).where(Admin.admin_id == 'root')

# # execution
# rs = session.execute(stmt).fetchall() # returns model object
# admin = rs[0][0]  # 첫 번째 튜플의 첫 번째 요소인 Admin 객체에 접근합니다.

# admin_id = admin.admin_id
# admin_pw = admin.admin_pw
# created_at = admin.created_at
# description = admin.description

# # 데이터 사용
# print(admin_id, admin_pw, created_at, description)



# from sqlalchemy import insert

# # insert method
# # stmt = (insert(Admin).values(admin_id='tired', admin_pw='1234'))
# # rs = session.execute(stmt)
# # session.commit()

# # client1 = User(id = 1234, name='김모씨', fullname='fullname존재..?')
# # session.add(client1)
# # session.commit()

# def sign_up(id, pw, created_at=None, description=None)

