# Python 
# Pydantic
# FastAPI
from typing import List
from fastapi import FastAPI
from fastapi import status

# Models
from models import User, UserLogin, UserOut
from models import Tweet

app = FastAPI()

# Path operations 

@app.get(
    path= '/',
    tags= ['Home']
    )
def home():
    return {'Twitter API': 'Working!!'}

## Users

### Register an user
@app.post(
    path = '/signup',
    response_model = User,
    response_model_exclude= {'password'},
    status_code = status.HTTP_201_CREATED,
    summary = 'Register a user',
    tags= ['Users']
)
def signup():
    pass

### Login an user
@app.post(
    path = '/login',
    response_model = UserLogin,
    response_model_exclude= {'password'},
    status_code = status.HTTP_200_OK,
    summary = 'Login a user',
    tags= ['Users']
)
def login():
    pass

### show all users
@app.get(
    path = '/users',
    response_model = List[User],
    response_model_exclude= {'password'},
    status_code = status.HTTP_200_OK,
    summary = 'Show all users',
    tags= ['Users']
)
def show_all_users():
    pass

### show an user
@app.get(
    path = '/users/{user_id}',
    response_model = User,
    response_model_exclude= {'password'},
    status_code = status.HTTP_200_OK,
    summary = 'Show a specific user',
    tags= ['Users']
)
def show_an_user():
    pass

### Delete an user
@app.delete(
    path = '/users/{user_id}/delete',
    response_model = User,
    response_model_exclude= {'password'},
    status_code = status.HTTP_200_OK,
    summary = 'Delete an user',
    tags= ['Users']
)
def Delete_an_user():
    pass

### update an user
@app.put(
    path = '/user/{user_id}/update',
    response_model = User,
    response_model_exclude= {'password'},
    status_code = status.HTTP_200_OK,
    summary = 'Update an user',
    tags= ['Users']
)
def update_an_user():
    pass

## Tweets

###show all tweets
@app.get(
    path= '/',
    response_model= List[Tweet],
    status_code= status.HTTP_200_OK,
    summary= 'Show all tweets',
    tags= ['Tweets']
    )
def home_tweets():
    return {'Twitter API Home': 'Working Good!!'}

###post a tweet
@app.post(
    path= '/post',
    response_model= Tweet,
    status_code= status.HTTP_201_CREATED,
    summary= 'Post a tweet',
    tags= ['Tweets']
)
def post():
    pass

###show a tweet
@app.get(
    path= '/tweets/{tweet_id}',
    response_model= Tweet,
    status_code= status.HTTP_200_OK,
    summary= 'Show a tweet',
    tags= ['Tweets']
)
def show_a_tweet():
    pass

###Delete a tweet
@app.delete(
    path= '/tweets/{tweet_id}/delete',
    response_model= Tweet,
    status_code= status.HTTP_200_OK,
    summary= 'Delete a tweet',
    tags= ['Tweets']
)
def delete_a_tweet():
    pass

###Update a tweet
@app.put(
    path= '/tweets/{tweet_id}/update',
    response_model= Tweet,
    status_code= status.HTTP_200_OK,
    summary= 'Update a tweet',
    tags= ['Tweets']
)
def update_a_tweet():
    pass

# Run server
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