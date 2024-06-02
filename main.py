from fastapi import FastAPI
from typing import List
from models import User, Gender, Role
from uuid import UUID

# app module
app = FastAPI()

# Create a virtual database as a list of Users 
db: List[User] = [
    User(
        id=UUID("674c0976-5e1f-4f51-ade9-fc0d042e0d7f"),
        first_name="Jamila",
        last_name="Ahmed",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=UUID("d963d03e-938b-4ec4-8a0e-714c8f5d2d93"),
        first_name="John",
        last_name="Doe",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    ),
    User(
        id=UUID("62ecd0fd-fe51-4dc5-b22c-95fd321b883a"),
        first_name="Alice",
        last_name="Smith",
        gender=Gender.female,
        roles=[Role.user]
    ),
    User(
        id=UUID("5e05a567-0725-46fa-85a7-e3fe4a40c2e9"),
        first_name="Bob",
        last_name="Brown",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=UUID("3ba6229e-f35a-4412-a912-5af153039bd2"),
        first_name="Clara",
        last_name="Davis",
        gender=Gender.female,
        roles=[Role.admin, Role.student]
    ),
    User(
        id=UUID("c3761019-1c8f-41eb-bf48-82022a73821f"),
        first_name="David",
        last_name="Miller",
        gender=Gender.male,
        roles=[Role.user, Role.student]
    ),
    User(
        id=UUID("09397f8f-371f-405d-940c-fc88d687b55f"),
        first_name="Eva",
        last_name="Wilson",
        gender=Gender.female,
        roles=[Role.user]
    ),
    User(
        id=UUID("8901e7e5-16bf-4e3a-9dd4-8047ea99bc39"),
        first_name="Frank",
        last_name="Moore",
        gender=Gender.male,
        roles=[Role.admin]
    ),
    User(
        id=UUID("b2ad5453-91a1-45fe-bb66-9ca8063215c6"),
        first_name="Grace",
        last_name="Taylor",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=UUID("99256205-f539-49f2-8b46-f5e8dbfb7e89"),
        first_name="Hannah",
        last_name="Thomas",
        gender=Gender.female,
        roles=[Role.user]
    )
]

# Get method for a root path
@app.get("/")
async def root():
    return {"Hello": "World"}

# Route to Get all the Users 
@app.get("/api/v1/users")
async def fetch_users():
    return db

# Create a post method to add a new user
@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    # Get the newly created user's uuid
    return{"id": user.id}

# Create a method to Delete a user instance
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return