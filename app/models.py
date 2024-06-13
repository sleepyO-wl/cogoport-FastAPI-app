from sqlalchemy import Column, Integer, String
from app.database import Base


# Define the Configuration model
class Configuration(Base):
    __tablename__ = "configurations"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)

    # Unique country code
    country_code = Column(String, unique=True, index=True)

    # Store requirements as JSON or a serialized string
    requirements = Column(String)
