from member.database import session
from member.Models import UserAccount

def user_signin(email, pw, name=None):
    user = UserAccount(email=email, pw=pw, name=name)
    session.add(user)
    session.commit()
    return True