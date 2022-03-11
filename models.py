# Python 
from uuid import UUID
from datetime import date, datetime
from typing import Optional 

# Pydantic
from pydantic import BaseModel, Field, EmailStr

# Models

class User(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(
        ...,
        min_length = 8,
        max_length = 64,
        example = 'example@example.com'
    )
    first_name: str = Field(
        ...,
    min_length = 1,
    max_length = 50,
    example = 'john'
    )
    last_name: str = Field(
        ...,
    min_length = 1,
    max_length = 50,
    example = 'Doe'
    )
    birth_date: Optional[date] = Field(default= None)


class UserLogin(User):
    password: str = Field(
        ...,
        min_length = 8,
        max_length = 40,
    )


class UserOut(User):
    pass


class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(...,
    min_length= 1,
    max_length= 256,
    example= 'Hello world'
    )
    created_at: datetime = Field(default= datetime.now())
    updated_at: Optional[datetime] = Field(default= None)
    by: UserLogin = Field(...)