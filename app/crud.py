from sqlalchemy.orm import Session
from app import models, schemas


# Retrieve a configuration by country code
def get_configuration(db: Session, country_code: str):
    return db.query(models.Configuration).filter(models.Configuration.country_code == country_code).first()


# Create a new configuration
def create_configuration(db: Session, config: schemas.ConfigurationCreate):
    db_config = models.Configuration(country_code=config.country_code, requirements=config.requirements)
    db.add(db_config)
    db.commit()
    db.refresh(db_config)
    return db_config


# Update an existing configuration
def update_configuration(db: Session, country_code: str, requirements: str):
    db_config = db.query(models.Configuration).filter(models.Configuration.country_code == country_code).first()
    if db_config:
        db_config.requirements = requirements
        db.commit()
        db.refresh(db_config)
    return db_config


# Delete a configuration by country code
def delete_configuration(db: Session, country_code: str):
    db_config = db.query(models.Configuration).filter(models.Configuration.country_code == country_code).first()
    if db_config:
        db.delete(db_config)
        db.commit()
    return db_config
