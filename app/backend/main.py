from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'Hello World'}