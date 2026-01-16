from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def get_home():
    return {"message" : "This is first time i am learning the ci/cd pipelines using the ci/cd syamsundar"}


