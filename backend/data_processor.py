import pandas as pd
from cryptography.fernet import Fernet
import os
import json  # Added for json.dumps

cipher = Fernet(os.getenv('SECRET_KEY').encode())

def process_uploaded_file(file_content, file_type):
    try:
        if file_type == 'csv':
            df = pd.read_csv(pd.io.common.BytesIO(file_content))
        elif file_type == 'xlsx':
            df = pd.read_excel(pd.io.common.BytesIO(file_content))
        elif file_type == 'pdf':
            import tabula
            df = tabula.read_pdf(pd.io.common.BytesIO(file_content), pages='all')[0]
        else:
            raise ValueError("Unsupported file type")

        # Standardize and extract data into a dict
        data_dict = {}
        # Assuming columns like 'Revenue', 'Expenses', etc. (case-insensitive)
        if 'revenue' in df.columns.str.lower():
            data_dict['revenue'] = df[df.columns[df.columns.str.lower() == 'revenue'][0]].sum()
        else:
            data_dict['revenue'] = 0  # Default if missing

        if 'expenses' in df.columns.str.lower():
            data_dict['expenses'] = df[df.columns[df.columns.str.lower() == 'expenses'][0]].sum()
        else:
            data_dict['expenses'] = 0

        # Add more fields as needed (e.g., 'taxes', 'loans') based on your requirements
        # For now, keep it simple

        # Encrypt the JSON string of the dict
        encrypted_data = cipher.encrypt(json.dumps(data_dict).encode())
        return encrypted_data.decode()
    except Exception as e:
        # Handle errors (e.g., invalid file) gracefully
        raise ValueError(f"Error processing file: {str(e)}")

def decrypt_data(encrypted_str):
    try:
        return cipher.decrypt(encrypted_str.encode()).decode()
    except Exception as e:
        raise ValueError(f"Error decrypting data: {str(e)}")