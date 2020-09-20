from datetime import datetime
from sqlalchemy.exc import IntegrityError

from fastapi import FastAPI, HTTPException

from worker import count
from models import Tasks, Results
from database import Session


app = FastAPI()


@app.post('/add_address/')
def create_item(address: str):
    task = Tasks(address=address, timestamp=datetime.utcnow())
    session = Session()
    session.add(task)
    try:
        session.commit()
    except IntegrityError:
        raise HTTPException(status_code=422, detail='Unprocessable Entity')
    count.delay(task.id)


@app.get('/results/')
def results():
    session = Session()
    results = session.query(Results).all()
    return {'results': results}
