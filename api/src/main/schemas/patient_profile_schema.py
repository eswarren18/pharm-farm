"""
Pydantic schemas for PatientProfile entity.

Defines the data validation and serialization models (schemas) for patient
profile API operations, such as creating and reading patient profiles. These
schemas ensure correct data structure in API requests and responses, and are
separate from database models.
"""

from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class PatientProfileBase(BaseModel):
    first_name: str
    last_name: str
    dob: date
    phone: str
    email: Optional[EmailStr] = None
    active: bool = False


class PatientProfileCreate(PatientProfileBase):
    pass


class PatientProfileRead(PatientProfileBase):
    id: int
    user_id: Optional[int] = None

    class Config:
        from_attributes = True
