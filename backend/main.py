from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from data_processor import process_uploaded_file, decrypt_data
from ai_analyzer import analyze_financial_health
from integrations import fetch_banking_data, fetch_razorpay_data
import json
import os

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...), industry: str = "Manufacturing"):
    data = process_uploaded_file(await file.read(), file.filename.split('.')[-1])
    decrypted = decrypt_data(data)
    data_dict = json.loads(decrypted)  # This should be {'revenue': value, 'expenses': value}
    insights = analyze_financial_health(data_dict, industry)
    return {"insights": insights, "data": data_dict}  # Ensure 'data' is included

@app.get("/integrate-banking")
def integrate_banking(user_id: int):
    return fetch_banking_data(user_id)

@app.get("/integrate-razorpay")
def integrate_razorpay(user_id: int):
    return fetch_razorpay_data(user_id)

# Add more endpoints as needed