from pydantic import BaseModel


# Base schema for configuration
class ConfigurationBase(BaseModel):
    country_code: str
    requirements: str  # Adjust type if you choose to store requirements differently


# Schema for creating a new configuration
class ConfigurationCreate(ConfigurationBase):
    pass


# Schema for returning configuration details
class Configuration(ConfigurationBase):
    id: int

    class Config:
        orm_mode = True
