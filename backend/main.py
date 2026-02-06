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

# ✅ CORS FIX (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://sanfintool-cl4ozy5ep-santhoshini-25s-projects.vercel.app",
        "https://sanfintool-ik32alewo-santhoshini-25s-projects.vercel.app",
        "https://sanfintool-c8q4uskrj-santhoshini-25s-projects.vercel.app",
        "https://*.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)
@app.get("/")
def root():
    return {"status": "Backend is running"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...), industry: str = "Manufacturing"):
    data = process_uploaded_file(await file.read(), file.filename.split('.')[-1])
    decrypted = decrypt_data(data)
    data_dict = json.loads(decrypted)

    insights = analyze_financial_health(data_dict, industry)

    return {
        "status": "success",
        "insights": insights,
        "data": data_dict
    }

@app.get("/integrate-banking")
def integrate_banking(user_id: int):
    return fetch_banking_data(user_id)

@app.get("/integrate-razorpay")
def integrate_razorpay(user_id: int):
    return fetch_razorpay_data(user_id)
