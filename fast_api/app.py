from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Olar, Mundo!"}


@app.get("/suco")
def read_suco():
    return {"message": "Suco de laranja"}
