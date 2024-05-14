from fastapi import Depends, FastAPI, HTTPException
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from sqlalchemy import text
import json

from . import model
from . import crud
from . import schema
from .database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI()
client = TestClient(app)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/v1/api_status")
def test_urls():
    response = client.get("/")
    response_countries = client.get("/v1/countries")
    response_by_country = client.get("/v1/countries/Greece")
    try:
        assert response.status_code == 200
        assert response_countries.status_code == 200
        assert response_by_country.status_code == 200
        return json.dumps({"status":"UP"})
    except Exception:
        return json.dumps({"status":"DOWN"})


@app.get("/")
async def read_root():
        return {"Countries": "hello"}

@app.get("/v1/countries")
async def read_country(db: Session = Depends(get_db)):
    db_countries = crud.get_countries(db)
    if db_countries is None:
        raise HTTPException(status_code=404, detail="not found")
    return db_countries

@app.get("/v1/countries/{country}")
async def get_by_country(country:str, db: Session = Depends(get_db)):
    db_countries = crud.get_data_by_country(db, country=country)
    if db_countries is None:
        raise HTTPException(status_code=404, detail="not found")
    return db_countries

@app.post("/records")
def create_records(records: schema.addRecords, db: Session = Depends(get_db)):
    return crud.add_records(db, records)

@app.delete("/v1/countries/{country}")
def delete_country(country:str, db:Session =  Depends(get_db)):
    delete = crud.delete_country(db, country)
    if delete:
        return json.dumps({"status":"DELETED"})
    else:
        return json.dumps({"status":"FAILED"})
