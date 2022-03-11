# Python 
# Pydantic
# FastAPI
from fastapi import FastAPI

# Models
from models import User, UserLogin, UserOut
from models import Tweet

app = FastAPI()

@app.get(
    path= '/',
    tags= ['Home']
    )
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