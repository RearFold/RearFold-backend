from fastapi import FastAPI
import crud

app = FastAPI()
app.include_router(crud.router)



# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8001)
