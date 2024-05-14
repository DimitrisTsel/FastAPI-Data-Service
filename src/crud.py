from sqlalchemy.orm import Session

from . import model
from . import schema
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError

def get_countries(db: Session):
    try:
        countries = db.query(model.Item.Country).distinct().all()
        return [country[0] for country in countries]
    except Exception as e:
        print(f"Error occurred: {e}")
        return []

def get_data_by_country(db:Session, country:str):
    try:
        data = db.query(model.Item).filter(model.Item.Country == country).all()
        return data
    except Exception as e:
        print(f"Error occurred: {e}")
        return []



def add_records(db: Session, records: schema.addRecords):
    try:
        records_dict = records.dict()
        db_record = model.Item(**records_dict)
        db.add(db_record)
        db.commit()
        #db.refresh(db_record)
        return db_record
    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        return None

def delete_country(db:Session, country:str):
    try:
        db.query(model.Item).filter(model.Item.Country == country).delete()
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Database error occurred: {e}")
        return False
    except HTTPException:
        raise HTTPException(
            status_code=404,
            msg=f"The country {country} does not exist"
        )
        return False
    return True