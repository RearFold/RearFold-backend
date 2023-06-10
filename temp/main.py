# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

########################################################################################

# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates

# app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")


# templates = Jinja2Templates(directory="templates")


# @app.get("/items/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse("item.html", {"request": request, "id": id}

import os
import uvicorn
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from member.crud import user_signin

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# @app.get("/", response_class=HTMLResponse)
# async def read_item():
#     return templates.TemplateResponse("index.html")

# ------------------------------------------------------------------------- controller

@app.get("/")
async def main():
    #print(root)
    with open(os.path.join('templates', 'index.html')) as fh:
        data = fh.read()
    return Response(content=data, media_type="text/html")

@app.get("/member/signup")
async def signup_html():
    #print(root)
    with open(os.path.join('templates/member', 'signup.html')) as fh:
        data = fh.read()
    return Response(content=data, media_type="text/html")

@app.get("/member/signin")
async def signin_html():
    #print(root)
    with open(os.path.join('templates/member', 'signin.html')) as fh:
        data = fh.read()
    return Response(content=data, media_type="text/html")



# ------------------------------------------------------------------------- API

@app.post("/member/signin/request")
async def true_html():
    #print(root)
    with open(os.path.join('templates/member', 'true.html')) as fh:
        data = fh.read()
    return Response(content=data, media_type="text/html")

@app.post("/member/signup/request")
async def request_signup(request: Request):
    # https://stackoverflow.com/questions/74318682/how-to-submit-html-form-input-value-using-fastapi-and-jinja2-templates
    form_data = await request.form()
    email = form_data.get("email")
    pw = form_data.get("pw")
    name = form_data.get("name")
    
    # 폼 데이터 사용
    print(email, pw, name)
    
    print()
    print(email, pw, name)
    if user_signin(email, pw, name):
        with open(os.path.join('templates/member', 'true.html')) as fh:
            data = fh.read()
        return Response(content=data, media_type="text/html")
    else:
        with open(os.path.join('templates/member', 'false.html')) as fh:
            data = fh.read()
        return Response(content=data, media_type="text/html")
    
# @app.get("/items/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, email: str, pw: str, name: str):
#     return templates.TemplateResponse("item.html", {"request": request, "id": id}    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)