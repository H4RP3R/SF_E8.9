from fastapi import FastAPI

from worker import count


app = FastAPI()
@app.post('/add_address/')
def create_item(address: str):
    res = count.delay(address)
    print(res)
