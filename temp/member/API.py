import os
from fastapi import FastAPI, APIRouter, Response

# from temp.login.database import SessionLocal
# from models import Question

# router = APIRouter(
#     prefix="/api/question",
# )


# @router.get("/list")
# def question_list():
#     db = SessionLocal()
#     _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
#     db.close()
#     return _question_list


# app = FastAPI()

# @app.get("/member/signup")
# async def signup():
#     #print(root)
#     with open(os.path.join('templates/member', 'signup.html')) as fh:
#         data = fh.read()
#     return Response(content=data, media_type="text/html")


# app = FastAPI()
# @app.get("/member/signup")
# async def signup():
#     #print(root)
#     with open(os.path.join('templates/member', 'signup.html')) as fh:
#         data = fh.read()
#     return Response(content=data, media_type="text/html")

# why....... how..........