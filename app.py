# This code is only for user interface application

from fastapi import FastAPI, Form, Request, Response, File, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
import uvicorn
import os
import aiofiles
import json
import csv
from src.helper import llm_pipeline

# initialize the fastapi
app = FastAPI()

# I have to define a mount directory.
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates") # it will load index.html file

@app.get("/") # reference:https://fastapi.tiangolo.com/
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request}) # taking the docuemnt from the user

# async is used to reflect new changes in the webpage


# ----Upload document part-----
# function - if some one will click on button (e.g. Generate Q&A) it will trigger "/upload" and then below function will be executed
@app.post("/upload")
async def chat(request: Request, pdf_file: bytes = File(), filename: str = Form(...)):
    base_folder = 'static/docs/'
    if not os.path.isdir(base_folder):
        os.mkdir(base_folder)
    pdf_filename = os.path.join(base_folder, filename)
    
    async with aiofiles.open(pdf_filename, 'wb') as f: # with the help of aiofiles we are saving any kind of pdf file.it will take as binary object and save as pdf (I am receiving binary and saving pdf)
        await f.write(pdf_file)
        
    response_data = jsonable_encoder(json.dumps({"msg": 'success' , "pdf_filename": pdf_filename}))
    res = Response(response_data)
    return res


#------Generate Q&A button part--------
# saving output in csv file
def get_csv (file_path):
    answer_generation_chain, ques_list = llm_pipeline(file_path) # llm_pipeline using or calling helper.py (calling both functions in helper.py)
    base_folder = 'static/output/'
    if not os.path.isdir(base_folder):
        os.makdir(base_folder)
    output_file = base_folder+"QA.csv"
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Question", "Answer"]) # Writing the header row
        
        for question in ques_list:
            print("Question: ", question)
            answer = answer_generation_chain.run(question)
            print("Answer: ", answer)
            print("---------------------------------------------------------\n\n")
            
            # save answer to csv file
            csv_writer.writerow([question, answer])
    return output_file



# Now i am going to write my final method. if my button is executed, above particular trigger (get_csv) will happen. I will create another function to analyze trigger

@app.post("/analyze")
async def chat(request: Request, pdf_filename: str = Form(...)):
    output_file = get_csv(pdf_filename)
    response_data = jsonable_encoder(json.dumps({"output_file": output_file}))
    res = Response(response_data)
    return res



# Now I launch my application. launch fastapi server

if __name__ == "__main__":
    uvicorn.run("app:app", host='0.0.0.0', port=8080, reload=True) #local host. uvicorn is package which will help to launch local server
    
    
    