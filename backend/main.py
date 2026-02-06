from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from data_processor import process_uploaded_file, decrypt_data
from ai_analyzer import analyze_financial_health
from integrations import fetch_banking_data, fetch_razorpay_data
import json
import os
import tempfile

app = FastAPI()

# ✅ Allowed origins (LOCAL + VERCEL)
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://sanfintool-4v3a2bgugug-santhoshini-25s-projects.vercel.app"
]

# ✅ CORS middleware (FIXED)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 👈 allow all for now
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Upload endpoint
@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    industry: str = "Manufacturing"
):
    # Read file safely
    contents = await file.read()

    # Process file (CSV / JSON / XLSX etc.)
    data = process_uploaded_file(contents, file.filename.split('.')[-1])

    # Decrypt processed data
    decrypted = decrypt_data(data)

    # Convert to dict
    data_dict = json.loads(decrypted)

    # AI analysis
    insights = analyze_financial_health(data_dict, industry)

    return {
        "status": "success",
        "insights": insights,
        "data": data_dict
    }

# ✅ Banking integration
@app.get("/integrate-banking")
def integrate_banking(user_id: int):
    return fetch_banking_data(user_id)

# ✅ Razorpay integration
@app.get("/integrate-razorpay")
def integrate_razorpay(user_id: int):
    return fetch_razorpay_data(user_id)

# ✅ Health check (VERY IMPORTANT for Render)
@app.get("/")
def health_check():
    return {"status": "Backend is running"}
