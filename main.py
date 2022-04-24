# Python 
# FastAPI
import json
from uuid import UUID
from typing import List
from fastapi import FastAPI, Body, status
from fastapi import Form, HTTPException
from pydantic.networks import EmailStr

# Models
from models import User, UserRegister, UserLoginOut 
from models import Tweet

app = FastAPI()

# Path operations 

## Users


### Register an user
@app.post(
    path = '/signup',
    response_model = User,
    status_code = status.HTTP_201_CREATED,
    summary = 'Register a user',
    tags= ['Users']
)
def signup(user: UserRegister= Body(...)):
    """
    Signup \n
    This path operation register an user in the app \n
    Parameters:
    - Request body parameters:
    - User: UserRegister \n
    Return a json with a basic user information:
    - UserID: UUID (Universal Unique Identifier)
    - email: EmailStr
    - first_name: str
    - last_name: str
    - birth_date: datetime
    """
    with open('users.json','r+', encoding= 'utf-8') as f:
        contents = json.loads(f.read())         #carga string transforma a json
        user_dict = user.dict()                 #convertir body en diccionario
        user_dict['user_id'] = str(user_dict['user_id'])
        user_dict['birth_date'] = str(user_dict['birth_date'])
        contents.append(user_dict)
        f.seek(0)                               #moverme al principio del archivo
        f.write(json.dumps(contents))           #transf un dict y escribo como un json 
        return user                             

# solo lee un usuario
### Login an user
@app.post(
    path = '/login',
    response_model = UserLoginOut,
    status_code = status.HTTP_200_OK,
    summary = 'Login a user',
    tags= ['Users']
)
def login(email: EmailStr = Form(...), password: str = Form(...)):
    """
    Login \n
    This path operation login an user in the app \n
    Parameters:
    - Request body parameters:
        - email: EmailStr
        - password: str 
    Return a json with a basic user information:
    - UserID: UUID (Universal Unique Identifier)
    - email: EmailStr
    - first_name: str
    - last_name: str
    - birth_date: datetime
    """
    with open("users.json", "r", encoding="utf-8") as f: 
        contents = list(json.loads(f.read()))
        for user in contents:
            if email == user["email"] and password == user["password"]:
                return UserLoginOut(email=email, message="Logged user!")
            else:
                return UserLoginOut(email=email, message= "Login not successful")


### Show all users
@app.get(
    path = '/users',
    response_model = List[User],
    status_code = status.HTTP_200_OK,
    summary = 'Show all users',
    tags= ['Users']
)
def show_all_users():
    """
    Users \n
    This path operation shows all users in the app \n
    Parameters:
    - \n
    Returns a json list with all users in the app, with the following keys:
    - user_id: UUID 
    - email: EmailStr
    - first_name: str
    - last_name: str
    - birth_date: datetime
    """
    with open('users.json', 'r', encoding = 'utf-8') as f:
        content = json.loads(f.read())
        return content

# solo lee un usuario
### Show an user
@app.get(
    path = '/users/{user_id}',
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = 'Show a specific user',
    tags= ['Users']
)
def show_an_user(user_id: UUID = (...)):
    """
    One User \n
    This path operation shows one user in the app if he or she exists\n
    Parameters:
    - User_id: UUID
    Returns a json with one user in the app, with the following keys:
    - user_id: UUID 
    - email: EmailStr
    - first_name: str
    - last_name: str
    - birth_date: datetime
    """
    with open('users.json', 'r', encoding = 'utf-8') as f:
        contents = json.loads(f.read())
        id= str(user_id)
        for user in contents:
            if user["user_id"] == id:
                return user
            else:
                raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f'The user_id does not exist'
        )


# solo lee un usuario
### Delete an user
@app.delete(
    path = '/users/{user_id}/delete',
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = 'Delete an user',
    tags= ['Users']
)
def Delete_an_user(user_id: UUID = (...)):
    """
    Delete an User \n
    This path operation delete one user in the app if he or she exists\n
    Parameters:
    - User_id: UUID
    Returns a json with deleted user data:
    - user_id: UUID 
    - email: EmailStr
    - first_name: str
    - last_name: str
    - birth_date: datetime
    """
    with open("users.json", "r+", encoding= "utf-8") as f: 
        contents = json.loads(f.read())
        id = str(user_id)
        for user in contents:
            if user["user_id"] == id:
                contents.remove(user)
                with open("users.json", "w", encoding="utf-8") as f:
                    f.seek(0)
                    f.write(json.dumps(contents))
                    return user
            else:
                raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f'The user_id does not exist'
        )


### Update an user
@app.put(
    path = '/user/{user_id}/update',
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = 'Update an user',
    tags= ['Users']
)
def update_an_user(user_id: UUID = (...), user: UserRegister= Body(...)):
    """
    Update an User \n
    This path operation update one user in the app if he or she exists\n
    Parameters:
    - User_id: UUID
    - Request body parameters:
        -User: UserRegister \n
    Returns a user model with the following data:
    - user_id: UUID 
    - email: EmailStr
    - first_name: str
    - last_name: str
    - birth_date: datetime
    """
    user_id= str(user_id)
    user_dict= user.dict()
    user_dict["user_id"] = str(user_dict["user_id"])
    user_dict["birth_date"] = str(user_dict["birth_date"])
    
    with open("users.json", "r+", encoding="utf-8") as f: 
        contents = json.loads(f.read())
    for user in contents:
        if user["user_id"] == user_id:
            contents[contents.index(user)] = user_dict
            with open("users.json", "w", encoding="utf-8") as f:
                f.seek(0)
                f.write(json.dumps(contents))
            return user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f'The user_id does not exist'
        )


## Tweets


###Show all tweets
@app.get(
    path= '/',
    response_model= List[Tweet],
    status_code= status.HTTP_200_OK,
    summary= 'Show all tweets',
    tags= ['Tweets']
    )
def home_tweets():
    """
    Users \n
    This path operation shows all tweets in the app \n
    Parameters:
    - \n
    Returns a json list with all tweets in the app, with the following keys
    - tweet_id: UUID
    - content: str
    - created_at: datetime
    - updated_at: Optional[datetime]
    - by: User 
    """
    with open('tweets.json', 'r', encoding = 'utf-8') as f:
        content = json.loads(f.read())
        return content


###Post a tweet
@app.post(
    path= '/post',
    response_model= Tweet,
    status_code= status.HTTP_201_CREATED,
    summary= 'Post a tweet',
    tags= ['Tweets']
)
def post(tweet: Tweet = Body(...)):
    """
    Post a Tweet \n
    This path operation post a tweet in the app \n
    Parameters:
    - Request body parameter
    - Tweet: Tweet \n
    Return a json with a basic tweet information:
    - tweet_id: UUID
    - content: str
    - created_at: datetime
    - updated_at: Optional[datetime]
    - by: User 
    """
    with open('tweets.json','r+', encoding= 'utf-8') as f:
        contents = json.loads(f.read())
        tweet_dict = tweet.dict()
        tweet_dict['tweet_id'] = str(tweet_dict['tweet_id'])
        tweet_dict['created_at'] = str(tweet_dict['created_at'])
        tweet_dict['updated_at']= str(tweet_dict['updated_at'])
        #casting UUID 
        tweet_dict['by']['user_id'] = str(tweet_dict['by']['user_id'])
        tweet_dict['by']['birth_date'] = str(tweet_dict['by']['birth_date'])
        contents.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(contents))
        return tweet





###Show a tweet
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
Pequeña validación para comprobar si el email ya existe.
if any(users['email'] == user.email for users in results):
            raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exist!"
        )
"""




"""
@validator('birth_date')  # Aqui está la magia
    def is_over_eighteen(cls, v):
        todays_date = datetime.date.today()
        delta = todays_date - v

        if delta.days/365 <= 18:
            raise ValueError('Must be over 18!')
        else:
            return v
En mi caso usé el validator decorator de Pydantic, al cual como puedes ver le paso como parametro el nombre del campo que quiero validar, lo uso para decorar una funcion de dos parametros (el primero es la clase misma NO una instancia, no la usaré pero la tengo que poner porque el validator es un classmethod y lo requiere), el segundo de ellos es el objeto a validar (pydantic al parecer tiene como convencion nombrarlo v). Implementas la logica del validador en esa funcion, la cual debe:

Elevar una exeption para cuando no es un dato correcto.
Retornar el dato mismo en caso de ser correcto.
Para todo esto debes importar de pydantic la funcion ‘validator’
"""