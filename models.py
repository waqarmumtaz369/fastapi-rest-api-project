from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

# Create a custom Gender type
class Gender(str, Enum):
    male = "male"
    female = "female"

# Create a custom Role type
class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

# Create a Data Class to store the User Instance in Database 
class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    gender: Gender
    roles: List[Role]