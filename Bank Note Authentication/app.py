import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import numpy as np
import pickle
import pandas as pd
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from fastapi import Request

app=FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")




pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post('/predict')
def predict_banknote(data:BankNote):
   data_dict = data.model_dump()
   variance = data_dict['variance']
   skewness = data_dict['skewness']
   curtosis = data_dict['curtosis']
   entropy = data_dict['entropy']
    
   prediction=classifier.predict([[variance,skewness, curtosis,entropy]])
   if(prediction[0]>0.5):
        prediction="Fake one"
   else:
        prediction="Its a bank note"
   return{
        'prediction': prediction
    }
    
if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1',port=8000)



