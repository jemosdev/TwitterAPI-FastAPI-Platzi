# Python 
from uuid import UUID
from datetime import date
from typing import Optional 

# Pydantic
from pydantic import BaseModel, EmailStr, Field 

# FastAPI
from fastapi import FastAPI

app = FastAPI()

# Models

class User(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(
        ...,
        min_length = 8,
        example = example@example.com
    )
    first_name: str = Field(
        ...,
    min_length = 1,
    max_length = 50
    )
    last_name: str = Field(
        ...,
    min_length = 1,
    max_length = 50
    )
    birth_date: Optional[date] = Field(default= None)

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)


class UserLogin(BaseModel):
    password: str = Field(
        ...,
        min_length = 8,
        example = example@example.com
    )


class Tweet(BaseModel):
    pass


@app.get(path= '/')
def home():
    return {'Twitter API': 'Working!!'}






if __name__ == '__main__':
    import uvicorn
    #uvicorn.run(app, host= 'localhost', port= 8000)
    uvicorn.run('main:app', host= 'localhost', port= 8000, reload= True)




"""
@validator('birth_date')  # Aqui está la magia
    def is_over_eighteen(cls, v):
        todays_date = datetime.date.today()
        delta = todays_date - v

        if delta.days/365 <= 18:
            raise ValueError('Must be over 18!')
        else:
            return v
"""