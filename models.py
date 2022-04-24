# Python 
from uuid import UUID
from datetime import date, datetime
from typing import Optional, List

# Pydantic
from pydantic import BaseModel, Field, EmailStr

# Models

# pendiente añadir default_factory para generar uuid
class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

#pendiente de borrar
class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length = 8,
        max_length = 40,
        example = '123456789'
    )


class User(UserBase):
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


class UserRegister(User, UserLogin):
    pass


class UserLoginOut(BaseModel): 
    email: EmailStr = Field(..., example = 'userexample@example.com')
    message: str = Field(..., example = '123456789')


class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(...,
    min_length= 1,
    max_length= 256,
    example= 'Hello world'
    )
    created_at: datetime = Field(default= datetime.now())
    updated_at: Optional[datetime] = Field(default= None)
    by: User = Field(...)