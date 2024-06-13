from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, models
from app.database import SessionLocal, engine

# Initialize the router
router = APIRouter()

# Create the database tables if they do not exist
models.Base.metadata.create_all(bind=engine)


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Endpoint to create a new configuration
@router.post("/create_configuration", response_model=schemas.Configuration)
def create_configuration(config: schemas.ConfigurationCreate, db: Session = Depends(get_db)):
    db_config = crud.get_configuration(db, country_code=config.country_code)
    if db_config:
        raise HTTPException(status_code=400, detail="Configuration already exists")
    return crud.create_configuration(db=db, config=config)


# Endpoint to get a configuration by country code
@router.get("/get_configuration/{country_code}", response_model=schemas.Configuration)
def get_configuration(country_code: str, db: Session = Depends(get_db)):
    db_config = crud.get_configuration(db, country_code=country_code)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_config


# Endpoint to update an existing configuration
@router.post("/update_configuration", response_model=schemas.Configuration)
def update_configuration(config: schemas.ConfigurationCreate, db: Session = Depends(get_db)):
    db_config = crud.update_configuration(db, country_code=config.country_code, requirements=config.requirements)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_config


# Endpoint to delete a configuration by country code
@router.delete("/delete_configuration", response_model=schemas.Configuration)
def delete_configuration(country_code: str, db: Session = Depends(get_db)):
    db_config = crud.delete_configuration(db, country_code=country_code)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_config
